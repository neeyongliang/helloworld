jQuery效果
------
## 隐藏和显示

语法:

> $(selector).hide(speed, callback);
> $(selector).show(speed, callback);

speed是元素变化的速度,取值可以是fast, slow, 或者毫秒数;callback是回调函数(可选);

在 jQuery1.9之前,还有 toggle() 来切换, DOM 的生成,修改都非常费时,因此尽量使用 show/hide

## 淡入/淡出

jQuery 有以下四种 fade() 方法, 参数同前:
- fadeIn()
- fadeOut()
- fadeToggle()
- fadeTo():透明度0~1之间.

## 滑动

jQuery 有以下滑动方法, 参数同前:
- slideDown()
- slideUp()
- slideToggle()

## 动画

jQuery animate()方法用于创建自定义动画.

> $(selector).animate((params), speed, callback);

params:必须参数,定义动画的 CSS 属性;

speed, callback 同前;

**提示**:可以用 animate 方法操作所有 CSS 属性,但必须使用驼峰(Camel)标识:

- padding-left <=> paddingLeft
- margin-right <=> marginRight

如果要生成颜色动画, 需要下载 Color Animator 插件.

*技巧*
>使用相对值: 需要在 CSS 属性前加入+=或者-=
>
>使用预定的值: 甚至可以把动画值定义为 slow,fast, 或者 toggle
>
>使用队列功能: 可以连续调用多个 animate()

## 停止动画

jQuery stop()方法适用于所有 jQuery 效果函数

**语法**:
>$(selector).stop(stopAll, goToEnd);

- stopAll: 可选,是否清除动画队列,默认 false;
- goToEnd: 可选,是否立即完成当前动画.

## callback 函数

由于 javascript 语句是逐一执行的,按照次序,动画之后可能会产生错误或页面冲突,因为动画还没有完成.为了避免这种状况,可以用参数的形式调用 callback 函数,在动画完成是执行.

**结论**: 如果希望动画完成后执行函数,请使用 callback.

## changing

通过 jQuery, 可以把动作/方法连接起来, changing 允许一条语句中又多个 jQuery 方法(在相同 的元素上)

>$("p1").css("color", "red").slideUp(2000).slideDown(2000);

jQuery 会去除多余的空格,所有可以回车换行.