##4.1 INSERT
###方法1：
- INSERT [INFO] tb_name [(col_name)] {VALUES|VALUE} ({expr|DEFAULT},...),(...)...

如果为采用自动编号的字段赋值，使用NULL或DEFAULT

###方法2：
- INSERT [INTO] tb_name SET col_name={expr|DEFAULT}...

注：与第一种方法的区别在于此方法使用了子查询。只能一次性插入一条。

###方法3：
- INSERT [INTO] tb_name [col_name,...] SELECT...

此方法可以插入到指定的数据表

##4.2 UPDATE
- UPDATE [LOW_PRIORITY] [IGNORE] tb_reference SET col_name1={expr|DEFAULT}[,col_name2={expr2|DEFAULT}]...[WHERE where_condition]

##4.3 DELETE
- DELETE FROM tb_name [WHERE where_condition]

##4.4 SELECT
- SELECT select_expr[,selec expr2...]
[
	FROM tb_references
	[WHERE where_condition]
	[GROUP BY {col_name|POSITION}[ASC|DESC]]
	[HAVING where_condition]
	[ORDER BY {col_name|expr|POSITION}[ASC|DESC]]
	[LIMIT {[offset] row_count|row_count OFFSET offset}]
]

##4.5 查询表达式
查询一个表达式表示想要的一个列，必须至少有一个。
多个列之间以英文逗号分隔。
星号*表示所有列。tb_name.*可以表示命名表的所有列。
查询表达式可以使用[AS] alias_name为其赋予别名。
命名可用于GROUP BY,ORDER BY或者HAVING子句。

##4.6 WHERE
记录进行过滤，如果没有指定where子句，则显示所有记录。在WHERE语句中，可以使用MySQL支持的函数与运算符。

##4.7 GROUP BY
- [GROUP BY {col_name|POSITION}[ASC|DESC]]

##4.8 HAVING
- [HAVING where_condition]

要使用HAVING要么是聚合函数，要么是确定其存在，只返回一个结果。

##4.9 ORDER BY
对结果进行排序

- [ORDER BY {col_name|expr|POSITION}[ASC|DESC]]

##4.10 LIMIT
限制查询返回结果数量

- [LIMIT{[offset] row_count|row_count OFFSET offset}]

LIMIT 2:返回头两个，
LIMIT 2,2:返回第3，4条记录。
PHP分页时会用的这个知识。