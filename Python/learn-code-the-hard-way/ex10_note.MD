# ex10_not.MD

------
##转义序列
下面列出了 Python 支持的所有转义序列。很多你也许不会用到，不过还是要记住它们的格式和功能。试着在字符串中应用它们，看看它们的功能。

|转义符       |功能     |
|--------   |-----:|
|\\ |Backslash()反斜杠|
|\' |Single quote(‘) 单引号|
|\" |Double quote(”) 双引号|
|\a |ASCII Bell(BEL) 响铃符|
|\b |ASCII Backspace(BS) 退格符|
|\f |ASCII Formfeed(FF) 进纸符|
|\n |ASCII Linefeed(LF) 换行符|
|\N{name} |Unicode 数据库中的字符名，其中 name 就是它的名字(Unicode only)|
|\r |ASCII CarriageReturn(CR)回车符|
|\t |ASCII Horizontal Tab(TAB) 水平制表符|
|\uxxxx |值为 16 位十六进制值xxxx 的字符(Unicode only)|
|\Uxxxxxxxx |值为 32 位十六进制值xxxx 的字符(Unicode only)转义符功能|
|\v |ASCIIVertical Tab(VT) 垂直制表符|
|\ooo |值为八进制值ooo 的字符|
|\xhh |值为十六进制数hh的字符|