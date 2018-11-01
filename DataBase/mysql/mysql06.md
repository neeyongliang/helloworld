##6.1 字符函数
|函数名称|描述|
|------|-----:|
|CONCAT()|字符连接|
|CONCAT_WS()|指定分隔符的字符连接|
|FORMAT()|数字格式化|
|LOWER()|小写|
|UPPER()|大写|
|LEFT()|获取左侧字符串|
|RIGHT()|获取右侧字符串|
|LENGTH()|字符串长度|
|LTRIM()|删除前导空格|
|RTRIM()|删除后续空格|
|TRIM()|删除空格符及特定字符串|
|SUBTRING()|字串|
|[NO] LIKE|匹配|
|REPLACE|代替|

###e.g.
SELECT CONCAT('A','B','-','C') -> AB-C
SELECT CONCAT_WS('|','A','B','C') ->A|B|C
LEFT('MySQL',2) ->My
SELECT LOWER(LEFT('MySQL',2)) -> my
RIGHT('MySQL') -> SQL
SELECT TRIM(LEADING/BOTH '?' FROM '??MySQL???') ->MySQL
SELECT REPLACE('??My??SQL???','??','!') ->!My!SQL!?
SELECT SUBSTRING('MySQL',1,2) 从“1”开始计数 ->My
SELECT ('MySQL',-1) ->L,长度不能为负值
SELECT 'MySQL' LIKE 'M%' ->1
SELECT * FROM test WHERE column1 LIKE '%_expr'
若搜索内容中有%，如tom%,则'%_expr'写成'%1%%'

##6.2 数值运算符
|函数名称|描述|
|------|-----:|
|CEIL()|向上取整(近1取整)|
|DIV|整数除法|
|FLOOR()|向下取整|
|MOD|取模|
|POWER()|幂运算|
|ROUND()|四舍五入|
|TRUNCATE()|数字截取|


##6.3 比较运算符
|函数名称|描述|
|------|-----:|
|[NOT] BETWEEN...AND...|[不]在范围内|
|[NOT] IN(...,...)|[不]在列出范围内|
|IS [NOT] NULL|是否为空|

##6.4 日期和时间函数
|函数名称|描述|
|------|-----:|
|NOW()|当前时间/日期|
|CURDATE()|当前日期|
|CURTIME()|当前时间|
|DATE_ADD()|日期变化、可加可减|
|DATEDIFF()|两个日期差值|
|DATE_FORMAT()|日期格式化|

##6.5 信息函数
|函数名称|描述|
|------|-----:|
|CONNECTION_ID()|连接ID|
|DATEBASE()|当前使用的数据库|
|LAST_INSERT_ID()|最后插入记录ID|
|USER()|当前用户|
|VERSION()|数据库版本|

##6.6 聚合函数
|函数名称|描述|
|------|-----:|
|AVG()|平均值|
|COUNT()|字数|
|MAX()|最大值|
|MIN()|最小值|
|SUM()|求和|

##6.7 加密函数
|函数名称|描述|
|------|-----:|
|MD5()|信息摘要(WEB)|
|PASSWORD()|修改密码|