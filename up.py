#!/bin/bash
import datetime
import os
import sys


def system():
    try:
        os.system(f'/usr/bin/python3 {path}/csdn.py >> {path}/logs/$(date +\%d-\%m-\%Y.txt)')
    except Exception as e:
        print(f'{e}\nsystem() 函数执行异常 请检查')


def main():
    global path
    # 获取当前路径
    path = sys.path[0]
    # 获取当前时间
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'当前路径 - {path}')
    print(f'开始运行 - {time}')
    if not os.path.isdir(f'{path}/logs/'):
        # 从 清华源 安装所需要用到的库
        os.system(f'pip install -r {path}/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple ')
        # 创建 日志 文件夹
        os.system(f'mkdir {path}/logs')
    else:
        pass

    if not os.system('ping www.baidu.com -c 1'):
        system()
        print(f"运行结束 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        os.system(
            f"echo 网络异常 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} >> {path}/logs/$(date +\%d-\%m-\%Y.txt)")
        print('网络异常 ...')


if __name__ == '__main__':
    main()
