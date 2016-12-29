初探css
------
## 定义和应用样式

CSS样式由一条或者多条声明组成.每一条声明都包含了属性和值两部分.

#### CSS 属性摘要

可能用到的属性: background-color, border, color, font-size, height, padding, text-decoration, width

#### 使用元素内嵌样式

> StyleInElements.html

#### 使用文档内嵌样式

> StyleInDocuments.html

#### 使用外部样式表

- 从其他样式表中导入样式

```
    // combined.css
    // @import可以有多个,并且要放置在最顶端
    @import "style.css"
    span {
        border: medium black dashed;
        padding: 10px;
    }
```

- 声明样式表的字符编码

```
@charset "UTF-8";
@import "style.css";
span {
    border: medium black dashed;
    padding: 10px;
}
```

## 样式的层叠与继承
#### 浏览器自带样式
#### 用户样式

例如Chrome的custom.css

#### 样式如何层叠

样式的所有层次分为:
- 1.元素内嵌样式(元素的全局属性style定义的样式)
- 2.文档内嵌样式(style 元素定义的样式)
- 3.外部样式(link元素导入的样式)
- 4.用户样式(用户自定义样式)
- 5.浏览器样式(默认样式)

#### 用重要的样式调整层叠次序

```
//文档内嵌样式
a {
    color: black !important;
}

//元素内嵌样式
a href="https://www.baidu.com" style="color:red;"
```

#### 根据具体程度和定义次序解决同级样式冲突问题

- 1.样式中选择器id的数目;
- 2.选择器中其他属性和伪类的数目;
- 3.选择器中元素名和伪元素的数目;
- 4.相同等级会被后面覆盖.

#### 继承

如果某个属性在相关样式中找不到,就会在父类中继承.

> CSSPropsInherit.html

与元素外观(文字颜色,字体等)会被继承;与元素在页面上的布局相关的样式不会被继承.此外,可以使用强制继承`inherit`.

> InheritExample.html
 
## CSS中的颜色

表示颜色的方法有很多:十进制,十六进制,名称, rgb 模式

## CSS中的长度
#### 绝对长度

cm, pt

#### 相对长度

- em: 与元素字号挂钩
- ex: 与元素字体的"x 高度"挂钩
- rem: 与根元素字号挂钩
- px: CSS 像素
- %: 另一属性值的百分比
- 以算式为值

```
p {
    background: grey;
    color: white;
    font-size: 20pt;
    width: calc(80% - 20px);
}
```

## 其他CSS单位
#### 使用CSS角度

单位标识|说明|
------|------|
deg|度(取值范围:0~360)|
grad| 百分度(取值范围:0~400)|
rad|弧度(取值范围:0~6.28rad)|
turn|圆周|

#### 使用 CSS 时间

秒s, 毫秒ms

## 测试 CSS 特性的支持情况

- http://caniuse.com
- Modernizr

## 有用的CSS工具

- 浏览器样式报告
- SelectorGadget
- 用LESS改进CSS
- CSS框架
