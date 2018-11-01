AJAX
-----
## load

>$(selector).load(URL, data, callback);

- URL: 必选,可以加参数细化选择
- data: 可选
- callback: 可选

> $("div").load("load_demo.txt #p1");
> 
> //将txt 里#p1 元素载入 div

可选的 callback 是 load 完成后的回调参数:
- responseText
- statusTXT
- xhr

## GET vs. POST

> $(selector).get(URL, callback);
> 
> $(selector).post(URL, data, callback); 