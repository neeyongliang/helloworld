NodeJS基础
------
## 什么是NodeJS

NodeJS就是一个用来解释JS等等解析器, 用途就是操作磁盘文件或者搭建HTTP服务器.

## 有啥用处

高性能web服务器: **事件机制**和**异步IO模型**

## 如何安装
#### 程序安装

官网: [NodeJS](https://nodejs.org)

#### 编译安装

下载源码包, 保证g++在6.4以上, python在2.6以上.

```shell
$ ./configure
$ make
$ sudo make install
```

## 如何运行

简单交互代码可以在命令行输入node运行, 复杂的代码可以是node + filename
```shell
$ node
$ node hello.js
```

#### 权限问题

Linux系统下, 使用NodeJS监控80或者443端口需要root权限.有下面两种方式:

```shell
$ sudo node server.js(推荐)
$ sudo chown root /usr/local/bin/node
$ sudo chmod +s /usr/local/bin/node(不推荐)
```

##模块

NodeJS允许自定义模块,编写每个模块都有require, exports, module三个预先定义好的变量可供选择.

#### require

require用于加载和使用别的模块, .js文件可以忽略文件名, 相对路径或者绝对路径都可以


```js
var foo1 = require('./foo');
var foo2 = require('./foo.js');
var foo3 = require('/home/user/foo');
var foo4 = require('/home/user/foo.js');

var data = require('./data.json');
```

#### exports

exports 对象是当前模块的导出对象,用于导出模块的公有方法和属性,被require使用.

```
export.hello = function() {
    console.log('Hello World!');
}
```

#### module

通过module对象可以访问到当前模块的一些相关信息，但最多的用途是替换当前模块的导出对象。

```
module.exports = function() {
    console.log('Hello World!');
};
```

#### 模块初始花

一个模块中的JS代码仅在模块第一次被使用时执行一次，并在执行过程中初始化模块的导出对象。之后，缓存起来的导出对象被重复利用。

#### 主模块

通过命令行参数传递给NodeJS以启动程序的模块被称为主模块。主模块负责调度组成整个程序的其它模块完成工作。

#### 完整示例

```js
//目录结构
- /home/user/hello
    - util/
        counter.js
    main.js

// counter.js
var i = 0;
function counter() {
    return ++i;
}

exports.count = count;

//main.js
var counter1 = require('./util/counter');
var counter2 = require('./util/counter');

console.log(counter1.count());
console.log(counter2.count());
console.log(counter2.count());

//结果
$ node main.js
1
2
3
```

counter.js并 **没有** 被require了两次而初始化两次.

## 二进制模块

虽然一般我们使用JS编写模块，但NodeJS也支持使用C/C++编写二进制模块。编译好的二进制模块除了文件扩展名是.node外，和JS模块的使用方式相同。


## 小结
- NodeJS是一个JS脚本解析器，任何操作系统下安装NodeJS本质上做的事情都是把NodeJS执行程序复制到一个目录，然后保证这个目录在系统PATH环境变量下，以便终端下可以使用node命令。

- 终端下直接输入node命令可进入命令交互模式，很适合用来测试一些JS代码片段，比如正则表达式。

- NodeJS使用CMD模块系统，主模块作为程序入口点，所有模块在执行过程中只初始化一次。

- 除非JS模块不能满足需求，否则不要轻易使用二进制模块，否则你的用户会叫苦连天。