##8.1 存储过程简介
SQL命令->MySQL引擎-(分析)->语法正确->可是别命令-(执行)->执行结果-(返回)->客户端
存储过程是SQL语句和控制语句的预编译集合，以一个名称存储并作为一个单元处理。

###优点：
- 增强SQL语句的功能和灵活性
- 实现较快的执行速度
- 减少了网路流量

##8.2 创建
###CREATE
[DEFINER={user|CURRENT_USER}]
PROCEDURE sp_name([proc_parameter[,...]])
[characteristic...] routine_body

proc_parameter
[IN|OUT|INOUT] param_name type

###参数
IN:表示该参数只能进不能出
OUT:输出
INOUT:可改变可返回

###过程体：
- 过程体由合法SQL语句的构成
- 过程体可以是任意的SQL(理论上，实际是增删改查连)
- 过程体如果为复合结构则使用BEGIN...END语句
- 复合结构可以包含声明，循环，控制结构。

##8.3 不带参数的存储过程
1)登录数据库
2)CREATE PROCEDURE sp1() SELECT VERSION();
3)调用CALL sp1[()]

调用：
CALL sp_name[()] 无参数可省括号
CALL sp_name([parameter[,...]])

##8.4 创建带有IN的存储过程
- SELECT * FROM USERS;
DELIMTER // 定界符
CREATE PROCEDURE removeUserById(IN p_id INT UNSIGNED)
BEGIN
DELETE FROM users WHERE id=p_id;
//
DELIMTER ;

##8.5 创建带有OUT的存储过程
- DELIMTER //
CREATE PROCEDURE f1(IN p_id INT UNSIGNED,OUT userNums INT UNSIGNED)
BEGIN
DELETE FROM users WHERE id=p_id;
SELECT count(id) FROM users INTO userNums;
END;
//
DELIMTER ;
CALL f1(27,@nums)
SELECT @nums

##8.6 创建多个OUT的存储过程
- DELIMTER //
CREATE PROCEDURE f2(IN p_age SMALLINT UNSIGNED,OUT deleteUser SMALLINT UNSIGNED,OUT userCounts SMALLINT UNSIGNED)
BEGIN
DELETE FROM users WHERE age = p_age;
SELECT ROW_COUNT INTO deleteUsers;
SELECT COUNT(id) FROM users INTO userCounts;
END;
//
DELIMTER ;