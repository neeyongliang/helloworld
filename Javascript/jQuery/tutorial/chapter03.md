HTML
------
## 获取内容和属性

获取内容:三个实用,简单的 DOM 操作方法:

- text()
- html()
- val():设置和返回表单字段.
- attr(): 用于获取属性值

>$(".link").attr("href");

## 设置内容和属性

也支持 text,html,val, 支持调用 attr() 同时设置多个属性,支持回到函数

>{"pro1":"v1","pro2":"v2"}

## 添加元素

主要有四个方法:

- append(): 被选取内容结尾处插入
- prepend(): 被选取内容开头处插入
- after(): 被选取内容之后处插入
- before(): 被选取内容之前处插入

## 删除元素

删除元素和内容,一般有两种方法:

- remove(): 删除被选中元素,可以使用过滤器
-  empty(): 清空该元素所有子节点

## 获取并设置 CSS 类

有如下方法:

- addClass()
- removeClass()
- toggleClass()
- css()

> $("p").css("font-size");
> 
> $("p").css({"background-color":"yellow", "font-size": "200%"});

## 尺寸
- width/height: 不包括内边距,边框,外边距
- innerWidth/innerHeight: 包括内边距
- outerWidth/outerHeight: 外边距