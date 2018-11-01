##2.1 复习
port：3306
超级用户：root
CREATE,ALTER,DROP

##2.2 数据库类型
###2.2.1 整型
TINYINT(8),SMALLINT(16),MEDIUMINT(24),INT(32),BIGINT(64)
**注**：没有绝对的类型，选择**合适**的。

###2.2.2 浮点型
FLOAT(m,n):m是总位数，n是小数点后位数
DOUBLE(m,n)

###2.2.3 时间类型
YEAR,TIME,DATE,DATETIME,TIMESTAMP(时间戳)
**注**：因为涉及时区，实际开发中用的少，一般采用数字类型。

###2.2.4 字符型
CHAR(m),VARCHAR(m),TINYTEXT,MEDIUMTEXT,LONGTEXT(基本不用)
ENUM('value1','value2',...) 枚举：最多65535个
SET('value1','value2',...) 集合：最多64个元素

##2.3 数据表
行：记录 
列：字段
###2.3.1 USE
- 打开数据库
- USE数据库


###2.3.2 创建数据库
CREATE TABLE [IF NOT EXISTS] table_name(
column1_name datatype [UNSIGNED][NOT NULL][PRIMARY KEY][AUTO_INCREMENT][UNIQUE KEY][FOREIGN KEY (col)][REFERENCES other_table],
column2_name...
)
分别表示：**无符号**、**非空**、**主码**、**自动编号**、**唯一**、**外码**、**参照**

###2.3.3 查看数据表
SHOW TABLES [FROM db_name][LIKE 'pattern'|WHERE exp]
exp:表达式

###2.3.4 查看数据结构
SHOW COLUMNS FROM tb_name

##2.4 操作数据库
###2.4.1 INSERT
INSERT [INTO] tb_name [(col_name1,col_name2,...)] VALUES (value1,value2,...)
**注**：若不写具体字段名，则value必须全写。

###2.4.2 SELECT
SELECT exp,... FROM tb_name

###2.4.3 AUTO-INCREMENT
- 自动编号，且必须与主键配合使用
- 默认情况下，初始值为1，可以为浮点型，但小说位数为0

##2.5 主键
主键约束，每张表只能有一个主键，主键保证记录的唯一性，主键自动NOT NULL

##2.6 UNIQUE KEY
唯一约束可以保证记录的唯一性，唯一约束字段可以为空值，一张表可以有多个唯一约束。

##2.7 默认约束 DEFAULT
- 默认值
- 当插入记录没有明确字段赋值，则自动赋予默认值
DEFAULT '默认值'

##2.8 复习
###数据类型：
字符型、整型、浮点型、日期时间类型
###数据表操作
插入记录
查找记录
###记录操作
创建数据表
约束作用