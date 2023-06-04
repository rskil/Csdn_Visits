import datetime
import random
import time
import os
import requests
import parsel
import threading

all_ip = []  # 所有代理ip
all_url = []  # 所有 url
Success_Number = 0  # 访问次数统计


def User_Agent():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    ]
    return random.choice(user_agent_list)


# 获取 CSDN 用户文章 向该方法传入 CSDN 用户名即可
# 例: https://blog.csdn.net/xxXXxxXX   xxXXxxXX 即为需要传入的参数
def Gain_url(username):
    url = f'https://blog.csdn.net/community/home-api/v1/get-business-list?page=1&businessType=blog&username={username}&size='
    headers = {"User-Agent": User_Agent()}
    total = requests.get(url=url, headers=headers).json()['data']["total"]  # 文章总数
    re = requests.get(url=url + f'{total}', headers=headers).json()['data']['list']  # 获取用户所有数据
    for i in re:  # 遍历所有文章url
        all_url.append(i['url'])  # url 存入数组

    if all_url is None:
        raise NameError("文章 URL 获取异常")
    return all_url


# 爬取免费代理
def Gain_ip89(Number):
    url = f'https://www.89ip.cn/index_'
    headers = {"User-Agent": User_Agent()}
    re = requests.get(url=url + str(Number) + '.html', headers=headers, timeout=2)
    # 转换数据类型
    selector = parsel.Selector(re.text)

    # 找到tr列表
    trs = selector.css(
        "body > div.layui-row.layui-col-space15 > div.layui-col-md8 > div > div.layui-form > table > tbody > tr")

    for tr in trs:
        ip_adder = tr.css("td:nth-child(1)::text").get().strip()
        ip_port = tr.css("td:nth-child(2)::text").get().strip()
        # ip_zt = tr.xpath("td:nth-child(4)::text").get()  # 过滤出高匿
        # if ip_zt == "高匿代理":
        all_ip.append(f'{ip_adder}:{ip_port}')
        # print(ip_adder + ":" + ip_port)
    print('.', end='')


def test_daili(Ip):
    global Success_Number
    # 写入字典
    proxy_dict = {
        "http": "http://" + Ip,
        "https": "http://" + Ip,
    }
    for url in all_url:
        try:
            headers = {"User-Agent": User_Agent()}
            cs = requests.get(url=url, headers=headers, proxies=proxy_dict, timeout=5)
            if cs.status_code == 200:
                Success_Number += 1
                print('Success', end='\t')

        except:
            # print(f'.', end='')
            pass


def main():
    # 获取用户所有文章
    Gain_url('xxXXxxXX') # 修改成自己的主页ID
    time.sleep(3)
    # 开始爬取代理地址
    print('免费代理爬取中...', end='')
    threads = []
    # Gain_ip89
    for ip_89 in range(40):
        T = threading.Thread(target=Gain_ip89, kwargs={"Number": ip_89})
        threads.append(T)
        try:
            T.start()
        except:
            pass

    # 等待所有线程任务结束。
    for t in threads:
        t.join()

    print("\n所有爬取代理线程完成")
    # print(all_ip)

    # 代理爬取完毕 开始访问测试
    print('开始访问...')
    test = []
    for i in all_ip:
        T = threading.Thread(target=test_daili, kwargs={"Ip": i})
        test.append(T)
        T.start()
    # 等待所有线程任务结束。
    for t in test:
        t.join()

    print("\n所有访问线程任务完成")
    print(f"成功访问次数为: {Success_Number}\n")


if __name__ == '__main__':
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    if not os.system('ping www.baidu.com -c 1'):
        main()

    else:
        print('网络不通 无法访问互联网 ...')
