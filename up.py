#!/bin/bash
import datetime
import os
import sys


def system():
    # 获取当前路径
    path = sys.path[0]
    # 获取当前时间
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print()
    print(f'当前路径 - {path}')
    print(f'开始运行 - {time}')

    if not os.path.isdir(f'{path}/logs/'):
        # 创建 日志 文件夹
        os.system(f'mkdir {path}/logs')

    try:
        os.system(f'/usr/bin/python3 {path}/csdn.py >> {path}/logs/$(date +\%d-\%m-\%Y.txt)')
    except Exception as e:
        print(f'{e}\nsystem() 函数执行异常 请检查')


if __name__ == '__main__':
    # 判断网络状态
    if not os.system('ping www.baidu.com -c 1'):
        system()
        print(f"运行结束 - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print('网络异常 ...')
