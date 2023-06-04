# Csdn_Visits

​	Csdn_Visits 通过爬取免费代理 批量 访问 CSDN 用户的文章 达到 增加 访问量 的目的



#### 目录结构

```shell
./
├── csdn.py		# 主文件
├── logs		# 运行 up.py 后创建 用于存储日志的文件夹
│   └── 00-00-0000.txt	# 日志
├── requirements.txt	# 需要用到的库
└── up.py		# 启动文件
```
<br>


#### 如何启动

```shell
pip -r ./requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple # 清华源进行安装

python ./up.py
```

> 启动前需要修改 `csdn.py`  内 `Gain_url('xxXXxxXX ')` 将 xxXXxxXX 修改为对应的 CSDN 用户 ID
>
> 例: https://blog.csdn.net/xxXXxxXX   xxXXxxXX 即为需要传入 `Gain_url` 函数的参数。

<br>


#### 写在最后

本项目仅供交流学习使用 ...
<br><br><br><br>
