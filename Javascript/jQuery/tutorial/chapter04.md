遍历
------
jQuery遍历,意为移动,根据其相对于其他元素的关系来查找或选取 html 元素.

jQuery 提供了多种方法,遍历 DOM, 其中最大的种类是树遍历( tree-traversal)

## 祖先

祖先是父, 祖父, 曾祖等等:
- parent(): 直接父元素
- parents(): 可带过滤
- parentsUtil(): 介于两个元素之间的所有

## 遍历后代
- children():直接子元素
- find()

## 同胞
- siblings(): 被选中的其他所有子同胞
-  next(), nextAll(), nextUtil();
-  prev(), prevAll(), prevUtil();

## 过滤
- first
- last
- eq: 返回被选元素带有指定元素的索引号(从0开始)
- filter: 符合条件的通过
- not: filter相反, 条件不通过
