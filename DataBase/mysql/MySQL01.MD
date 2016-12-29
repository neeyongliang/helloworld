#note about MySQL in imooc
------

#初涉MySLQ
##1.1 mysql概述
开源、原公司被Oracle收购，分为社区版和企业版

##1.2 安装、配置
###安装
官网下载，正常的安装。
安装之后，找到安装目录的配置想到文件(Configuration Wirzed)，选择As Windows serverce

###MySQL目录结构
bin目录：可执行文件
data目录：存储数据文件
docs目录：文档
include目录：存储包含的头文件
lib目录：存储类文件
share目录：错误消息和字符集文件

###修改编码方式
my.ini
[Client]
port:3306
[mysql]
defaut-character-set = utf8
[mysqld]
character-set-server = utf8
**不是utf-8！！**

##1.3 启动和停止服务
图形化：服务->mysql->(右键)启动、关闭
命令行：net start mysql
		net stop mysql

#使用mysql
##1.4 登录与退出
###mysql登录参数：
-v  :  --version
-u  :  --user-name
-p  :  --password[=name]
-P  :  --port=#
-h  :  --host-name
-D  :  --database=name
--delimiter=name 指定分隔符
--prompt=name 设置提示符

mysql -uroot -p -P3306 -h127.0.0.1
myslq>

###mysql退出
myslq> exit;
myslq> quit;
myslq> \q;

##1.5 修改mysql提示符
###方法1：连接客户端通过参数修改
shell>mysql -uroot -proot --prompt \h
localhost>(默认是mysql>)

###方法2：连接客户端之后，通过prompt修改
mysql>prompt 提示符
例如：prompt \u@\h \d \D>
\D  :  完整日期
\d  :  数据库
\h  :  主机名
\u  :  当前用户
（还有很多）

##1.6 myslq常用命令及语法规范
SELECT VERSION();显示当前服务器版本
SELECT NOW();显示当前时间
SELECT USER();显示当前用户

###规范：

 - 关键字与函数名称全部大写
 - 数据库名、表名、字段名全部小写
 - MySQL语句必须以；或者\g结尾

##1.7操作数据库
###创建数据库
CREATE {DATABASE | SCHEME} [IF NOT EXISTS] db_name [DEFAULF] CHARACTER SET [=] chartset_name
使用IF NOT EXISTS会忽略错误，产生警告
SHOW CHARSET db_name;显示编码方式
例：创建t2并用gtk编码
CREATE DATABASE IF NOT EXISTS t2 CHARACTER SET gtk;

###修改数据库
ALTER {DATABASE | SCHEME} [IF NOT EXISTS] db_name [DEFAULF] CHARACTER SET [=] chartset_name

###删除数据库
DROP {DATABASE | SCHEME} [IF EXISTS] db_name