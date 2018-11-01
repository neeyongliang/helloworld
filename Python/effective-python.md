Effective Python 笔记
------

01. 确认自己所用的 Python 版本
02. 遵循PEP8风格指南
03. 了解 bytes、str 与 unicode 的区别
```
    Python3: bytes 和 str;
    Python2: str 和 unicode;
```
04. 用辅助函数来取代复杂的表达式
05. 了解切割序列的办法

以0开头或 end 结尾的切割，要省略；

06. 在单次切片操作内，不要同时指定 start、end 和 stride
```
    三者不要同时使用；尽量避免负数步长；如果同时需要：
    A. 考虑首次切割范围；再次切割步长
    B. 使用 itertools 模块中的 islice
```
07. 用列表推导式来取代 map 和 filter
08. 不要使用含有两个以上表达式的列表推导
09. 使用生成器表达式来改写数据量较大的列表推导
```
    列表: $ value=[len(x)forxinopen('/path/some/file')]
    生成器: $ it=(len(x)forxinopen('/tmp/my_file.txt'))
           $ next(it)
```
10. 尽量用enumerate取代range
11. 用zip函数同时遍历两个迭代器
12. 不要在for和while循环后面写else块
13. 合理利用 try/except/else/finnally 结构中的每个代码块
14. 尽量使用异常来表示特殊情况,而不要返回 None
    抛出异常要写进开发文档中;
15. 了解如何在闭包里使用外围作用域中的变量
16. 考虑用生成器来改写直接返回列表的函数
17. 在参数上面迭代时,要多加小心
18. 用数量可变的位置参数减少视觉杂讯(*args)
    绝对不要给生成器使用 *args;如果出现 bug,难以排查
19. 用关键字参数来表达可选的行为
20. 用 None 和文档字符串来描述具有动态默认值的参数
21. 用只能以关键字形式指定的参数来确保代码明晰
```
    Python3有明确语法支持关键字形式指定的参数;
    Python2的函数可以指定**kwargs参数,并手动抛出TypeError异常来模拟
    #python3
    可以传递参数ignore_overflow=False. 
    #python2手动解析
    Ignore_overflow=kwargs. pop('ignore_overflow',False)
```
22. 尽量用辅助类来维护程序的状态,而不要用字典和元组
23. 简单的接口应该接受函数,而不是类的实例
24. 以 @classmethod 形式的多态去通用的构建对象
25. 用 super 初始化父类
26. 只在使用 Mix-in 组件制作工具类时使用多重继承
27. 多用 public 属性,少用 private 属性
28. 继承 collections. abc 以实现自定义的容器类型
29. 用纯属性取代 get 和 set 方法

    灵活使用 @property 来定义这种行为:遵循最小惊讶原则,需要快速执行

30. 考虑用 @property 来代替属性重构
    如果 @property 使用的太过频繁,就应该考虑彻底重构这件事
31. 用描述符来改写需要复用的 @property 方法
32. 用 __getattr__, __getattribute__ 和 __setattr__ 实现按需生成的属性

    __getattr__: 在访问不存在的属性是触发;
    __getattribute__: 每次访问属性时触发;

33. 使用元类来验证子类
34. 使用元类来注册子类
35. 使用元类来注解类的属性
36. 使用 subprocess 模块来管理子进程
37. 可以用线程来执行阻塞式 I/O,但不要用它做平行计算
38. 在线程中使用 Lock 来防止数据竞争
39. 使用 Queue 来协调各线程之间的工作
40. 考虑用协程来并发地运行多个函数
41. 考虑用 concurrent. futures 来实现真正的平行计算
42. 使用 functools. wraps 定义函数修饰器
43. 考虑以 contextlib 和 with 语句来改写可复用的 try/finally 代码
44. 用 copyreg 实现可靠的 pickle 操作
45. 应该用 datetime 模块来处理本地时间,而不是用 time 模块
46. 使用内置算法与数据结构
47. 在重视精度的场合,应该使用 decimal
48. 学会安装由 Python 开发者社区构建的模块
49. 为每个函数、类和模块编写文档字符串
50. 用包来安装模块，并提供稳固的 API
51. 为自编的模块定义根异常，以便将调用者与 API 相隔离
52. 用适当的方式打破循环依赖关系
53. 用虚拟环境隔离项目，并重建其依赖关系
54. 考虑用模块级别的代码来配置不同的部署环境
55. 通过 repr 字符串来输出调试信息
56. 用 unittest 来测试全部代码
57. 考虑用 pdb 实现交互调试
58. 先分析性能，然后再做优化
59. 用 tracemalloc 来掌握内存的使用及泄漏情况