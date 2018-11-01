##7.1 自定义函数
两个必要条件：
1)参数
2）返回值

##7.2 创建
- CREATE FUNCTION function_name
- RETURNS
{STRING|INTEGER|REALI|DECIMAL}
routine_body

##7.3 无参
- CREATE FUNCTION f1() RETURNS VARCHAR(20)
- RETURN DATE_FORMAT(NOW(),'%Y年/%m月%d日 %H时:%i分:%s秒')

DELIMTER修改定界符

##7.4 关于函数体
- 函数体由合法的SQL语句构成
- 函数体可以是最简单的SELECT或INSERT语句
- 函数体如果为复合结构则使用BEGIN...END语句
- 复合结构可以包含声明，循环，控制结构。
