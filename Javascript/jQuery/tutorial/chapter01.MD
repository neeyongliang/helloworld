tutorial
------
## 简介
jQuery是一个 javascript 库,包含以下特性:
- HTML元素选取
- HTML元素操作
- CSS操作
- HTML事件函数
- JS特效与动画
- HTML DOM 遍历与修改
- AJAX
- Utilities

## 安装
- 本地加载
- CDN 加载(好处: 其他网站可能加载过jQuery;从用户最近的CND加载)

## 语法
jQuery语法是为了 HTML 元素的选取编制的,可以对元素执行某些操作.

基础语法是: $(selector).action()
美元符定义jQuery,选择器选取对象, jQuery的 action 执行元素操作
jQuery位于 document.ready 函数中;

## jQuery选择器
- jQuery 元素选择器
- jQuery 属性选择器
- jQuery CSS选择器

如:$(".test").css("background-color", 'red');

## jQuery事件
jQuery 事件处理方法是 jQuery 中的核心函数。

最好把 jQuery 函数放到独立的 .js 文件中.

关于命名冲突:如果$被占用,那么使用 noConflict()处理该问题.

> var jq = jQuery.noConflict();

当然, 也可以直接用 jQuery
## 结论
由于 jQuery 试了处理 HTML 事件而特别设计的,那么当遵循以下原则:
- 把所有的 jQuery代码置于事件处理函数中;
- 把所有的事件处理函数置于文档就绪处理器中;
- 把 jQuery代码置于单独的文件中;
- 如果存在命名冲突,则重命名 jQuery 函数.

