##3.1 约束
- 约束保证数据的完整性和一致性
- 约束分为表级约束，列级约束
- 约束类包括：
	- NOT NULL：非空约束
	- PRIMARY KEY：主键约束
	- UNIQUE KEY：唯一约束
	- DEFAULT：默认约束
	- FOREIGN KEY：外键约束

###3.1.1 外键约束
- 保证数据的一致性、完整性
- 实现一对一或者一对多

###3.1.2 使用外键约束的要求
- 父表与子表必须使用相同的存储引擎，而且禁止使用临时表
- 数据表的存储引擎只能是InnoDB
- 外键列和参照列必须具有相似的数据类型，其中数字的长度、是否有符号位必须相同，而字符长度可以不同
- 外键列和参照列必须创建索引。如果外键列不存在索引的话，MySQL将自动创建索引。

###3.1.3 文件默认的存储引擎
my.ini
	default-storage-engine=INNODB
例子：
USE test;
CREATE TABLE provinces(
	id SMALLINT UNSIGNED PRIMARY KEY AUTO_INCREMENT
	//参照列
	//父表
	pname VARCHAR(20) NOT NULL 
	)
CREATE TABLE users(
	id SMALLINT UNSIGNED PRIMARY KEY AUTO_INCREMENT
	username VARCHAR(20) NOT NULL
	pid SMALLINT(相同) UNSIGNED(相同) 
	//自动创建索引
	//外键列
	//子表
	FOREIGN KEY(pid) REFERENCES provinces(id)  
)

##3.2 外键约束的参照操作
- CASECADE：从父表删除或者更新且自动删除或者更新子表匹配的行
- SET NULL：从父表删除或更新行，并且设置子表中的外键列
- RESTRICT：拒绝对父表删除或者更新操作
- NO ACTION：标准SQL的关键字，在MySQL与RESTRICT相同

注：很少使用物理约束，大多数使用逻辑约束(不使用FORENGN KEY)

##3.3 表级约束和列级约束
对一个数据列建立的约束，称为列级约束。
对多个数据列建立的约束，称为表级约束。
列级约束既可以在定义时声明，也可以在定以后声明；表级约束只能在定以后声明。

##3.4 修改数据表 
###添加单列
- ALTER TABLE tb_name ADD [COLUMN] col_name column_definition [FIRST|AFTER col_name]

###添加多列
- ALTER	 TABLE tb_name (col_name1 column_defition1,...)

不能指定位置关系。

###删除单行
- ALTER TABLE tb_name DROP col_name

###删除多行
- ALTER TABLE tb_name DROP col_name1,DROP col_name2,...

###添加主键约束
- ALTER TABLE tb_name ADD [CONSTRAINT[symbol]] PRIMARY KEY [index_type](index_col_name,...)

###删除主键约束
- ALTER TABLE tb_name DROP PRIMARY KEY

###删除唯一约束
- ALTER TABLE tb_name DROP {INDEX | KEY} index_name

###删除外键约束
- ATLTER TABLE tb_name DROP FOREIGN KEY fk_symbol

##3.4 修改数据表
### 修改列定义
- ALTER TABLE tb_name MODIFY [COLUMN] col_name column_definition [FIRST | AFTER col_name]

### 数据表更名
方法1：

- ALTER TABLE tb_name RENAME [TO|AS] new_tb_name

方法2：

- RENAME TABLE tb_name TO new_tb_name[,tb_name2 TO new_tb_name2,...]

##3.5 小结
1.约束:
	1)功能：
		a)NOT NULL
		b)PRIMARY KEY
		c)UNIQUE KEY
		d)DEFAULT
		e)FOREIGN KEY
	2)数据列的数目
		a)表级约束
		b)列级约束
2.修改数据表
	1)针对字段的操作：添加/删除字段、修改列定义，修改列名称
	2)针对字段的操作：添加/删除各种约束
	3)针对字段的操作：数据表更名(两种方式)