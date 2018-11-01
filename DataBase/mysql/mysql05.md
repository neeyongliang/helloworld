##5.1 子查询
Subquery,是指出现在其他SQL语句内的SELECT子句。
要求：
子查询嵌套在查询内部，且必须始终出现在圆括号内；
子查询可以包含多个关键字或者条件，如：DISTINCT,GROUP BY,ORDER BY,LIMIT,函数等；
子查询外层查询可以是：SELECT,INSERT,UPDATE,SET或者DO.
返回结果：
标量，一行，一列或子查询。

##5.2 子查询相关
###5.2.1 使用比较运算符的子查询
>,<,=,...,!=,<>
结构：operand comparison_operator(多条ANY|SOME|ALL) subquery

|类目|ANY|SOME|ALL|
|---------|-----:|:-----:|:-----:|
|>,>=|MIN|MIN|MAX|
|<,<=|MAX|MAX|MIN|
|=|任意|任意||
|<>,!=|||任意|

###5.2.2 由[INTO] IN/EXISTS引发的子查询
operand comparison_operator [NOT] IN (subquery)
=ANY运算符与IN等效
!=ANY或者<>ANY运算符与NOT IN等效
如果子查询返回任何行，EXISTS将返回TRUE,否则FALSE

##5.3 多表更新
UPDATE tb_references
SET col_name1 = {expr|DEFAULT}[,col_name2={expr2|DEFAULT}]
...
[WHERE where_condition]

参照关系：
tb_reference
{[INNER|CROSS] JOIN | {LEFT|RIGHT} [OUTER] JOIN}
table=reference
ON conditional_expr

##5.4 多表更新一步到位
创建数据表同时将查询结果插入到数据表
CREATE TABLE [IF NOT EXISTS] tb_name
[(create_defition,...)]
select_statement.

##5.5 连接
MySQL在SELECT语句中，多表更新，多表删除语句中支持JOIN操作。
###语法
- table_reference
- {[INNER|CROSS]JOIN|{LEFT|RIGHT}[OUTER]JOIN}
- tb_reference
- ON conditional_expr

##5.6 数据表参照
- table_reference
- tb_name [[AS] alias]|tb_subquery [AS] alias

此操作可以赋予别名

tb_subquery可以作为子查询使用在FROM子句中，这样的子查询必须为其赋予别名

##5.7 连接类型
###5.7.1 内连接(INNER JOIN)
	在MySQL中，JOIN CROSS,JOIN,INNER JOIN是等价的。
###5.7.2 左外连接LEFT (OUTER) JOIN
###5.7.3 右外连接RIGHT (OUTER) JOIN
	使用ON关键字来设定连接条件，使用WHERE关键字进行结果集过滤
	内连接表示两表重复的部分；
	左外表示左边全部+右边符合的；
	右外表示右边全部+左边符合的。

###5.7.4 多表连接
- SELECT (column1,column2,...) FROM tb_a AS A INNER JOIN tb_b AS B ON A.column1 = B.column2
- INNER JOIN tb_c AS C ON C.column2 = B.column2

###5.7.5 无限分类表设计：
CREATE TABLE test(
	id SMALLINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(20) NOT NULL,
	parent_id SMALLINT INT UNSIGNED NOT NULL,DEFAULT 0
);

|id|name|parent_id|
|------|-----:|:-----:|
|1|家电|0|
|2|电脑|0|
|3|大家电|1|
|4|电风扇|1|
|5|电脑|2|
|6|电脑配件|5|

###5.7.6 自连接
- SELECT s.id,s.name,p.name FROM test AS S
- JOIN test AS P ON s.parent_id = p.id