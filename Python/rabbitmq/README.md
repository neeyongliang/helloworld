Rabbit 环境搭建
---------------

## 安装

rabbitmq-server、erlang

## 启动服务 

sudo rabbitmq-server

# 安装插件

sudo rabbitmq-plugins enable rabbitmq_management

```text
4369 -- erlang发现口
5672 --client端通信口
15672 -- 管理界面ui端口
25672 -- server间内部通信口
```

xdg-open http://localhost:15672

## 常见错误
1. 发送不起效果
- 服务运行需要开放 5672 端口
- 服务运行至少需要 200 MB 空闲内存，可以在配置中修改 disk_free_limit 的值来改变

2. 无法远程连接服务器
- rabbitmq 默认只会创建 guest 账户，从 3.3 版本开始，guest 账户只能本地连接。

```shell
sudo rabbitmqctl add_user test 123456
sudo rabbitmqctl set_user_tags test administrator
sudo rabbitmqctl  set_permissions  -p  '/'  test '.' '.' '.'
sudo systemctl restart rabbitmq-server
```

3. 忘记消息回执
- 一个非常容易犯的错误就是忘记发送消息回执 basic_ack，导致内存越来越大。
- 为了 debug 这种错误，可以使用 rabbitmqctl 来打印 messages_unacknowleged 域

