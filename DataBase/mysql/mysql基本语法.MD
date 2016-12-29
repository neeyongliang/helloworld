#MySQL基本语法
##1.启动和关闭
###方法一：
启动服务：
```mysql
#cd /usr/bin
#./mysqld_safe&
```
关闭服务：
```mysql
# mysqladmin -uroot shutdown
```
###方法二：
若mysql是用RPM包安装
```mysql
#service mysql [option]
（有的版本mysql可能是service mysqld...）
start 启动
restart 重启
stop 关闭
```
-----

##2.连接
启动服务之后，需要连接。
```mysql
mysql -uroot -p
>mysql
```
其中，myql是应用名，-u之后是使用者身份，-p表示带密码.
每一行需要以；或者\g
help或者\h获得帮助
\c清除buffer

------
#DDL
##3.创建数据库
```mysql
CREAT DATABASE DBNAME;
show database;可查看已有数据库
use dbname;将要使用数据库
```

##4.删除数据库
```mysql
drop database dbname;
```

##5.创建表
```mysql
CREATE TABLE tablename(列1名,列1数据类型,约束条件,列2名...)
```

##6.查看表
```mysql
DESC tablename;
有时候也通过查看创建表:
mysql>show create table tablename \G;
\G 表示记录按照字段竖直排列
```

##7.删除表
```mysql
DROP TABLE table
```

##8.修改表
###(1)语法
```mysql
ALTER TABLE tablename MODIFY [COLUMN] column_definition [FIRST|AFTER col_name]
```
###(2)增加字段
```mysql
ALTER TABLE tablename ADD [COLUMN] column_definition [FIRST|AFTER col_name]
```
###(3)删除字段
```mysql
ALTER TABLE tablename DROP [COLUMN] col_name
```
###(4)字段改名
重命名时，CHANGE给定旧的和新的列名称和列当前的类型，即使旧的和新的列名称是一样的。
```mysql
ALTER TABLE tablename CHANGE [COLUMN] old_col_name col_new_name column_definition [FIRST|AFTER col_name]
```
###(5)修改字段排列顺序
前面的FIRST就是最前，ADD默认把新字段加到最后，其他的不改变。
###(6)改表名
```mysql
ALTER TABLE tablename RENAME [TO] new_tablename
```

------
#DML
##9.插入
```mysql
INSERT INTO tablename (field1,field2,...) VALUES (value1,value2...)
```
若value*顺序与field一致，field*可不写

##10.更新记录
```mysql
UPDATE tablename SET field1=value1,...,fieldn = valuen[WHERE CONDITION]
```
##11.删除记录
```mysql
DELETE FROM tablename [WHERE CONDITION]
```
##12.查询记录
###(1)查询不重复
```mysql
SELECT DISITINCE field FROM tablename
```
###(2)条件查询
```mysql
WHERE =,,>,<,>=,<=,!=
以及 OR，AND
```
###(3)排序和限制
```mysql
SELECT * FROM tablename ORDER BY field1,field2,...,[LIMIT 参数]
其中参数举例：
LIMIT 3表示前3个记录
LIMIT m,nn是指从第m+1条开始，取n条
```
###(4)聚合
```mysql
SELECT [field1,...,fieldn] func_name
FROM tablename
[WHERE where_condition]
[GROUP BY field1,field2,...]
[WITH ROLLUP]
[HAVING where_condition]
```
说明：
func_name表示要做的聚合操作，即聚合函数。sum(求和) count(*) max(最大值)
min(最小值)
group by分类
with rollup可选语法，表明是否对分类后再汇总
having表示对分类后结果再条件过滤
比较：
where先过滤再聚合（推荐）
having先聚合再过滤
###(5)表连接
内连接:(推荐)
```mysql
select a,b from table_a,table_b where table_a.field = table_b.field.field
```
外连接：
    左外连接：
```mysql
select a,b from table_a left join table_b on table_a.field = table_b.field
```
右外连接：
```mysql
select a,b from table_b left join table_a on table_a.field = table_b.field
```
###(6)子查询
把where的条件换为一个查询
注意：子查询和表连接之间的转换主要应用在两个方面：
mysql4.1以前的版本不支持子查询，只能用表连接；
表连接在很多情况下用于优化子查询。
###(7)记录联合
UNION|UNION ALL上下联合，join是左右联合

------
#DCL
DCL语句主要是DBA用来管理系统中的对象权限时所使用，一般开发人员很少使用。
grant授权
revoke收回权限

------
#帮助的使用
遇到问题可以快速查阅
```mysql
mysle>？ <要查阅的内容>
```