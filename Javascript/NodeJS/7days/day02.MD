代码的组织与部署
------

有经验的程序员编写一个程序首先从make文件写起.
同样的,使用NodeJS编写程序前,为了有一个良好的开端,要对代码组织与部署.

## 模块路径解析规则

`require` 函数除了相对路径和绝对路径, 还支持 `路径解析规则`.

- 1.内置模块

如果传递给require函数的是NodeJS内置模块名称,
不做路径解析,直接返回内部模块导出对象.例如require('fs')

- 2.node_modules目录

NodeJS定义了一个特殊的node_modules目录用于存放模块.使用路径规则会依次尝试以下路径:

```
/home/user/node_modules/foo/bar
/home/node_modules/foo/bar
/node_modules/foo/bar
```

- 3.NODE_PATH环境变量

与PATH环境变量类似,NodeJS通过NODE_PATH环境变量来指定额外的模块搜索路径.
NODE_PATH环境变量中包含一到多个目录路径,路径之间在Linux下使用`:`分隔,Windows下使用`;`

## 包

多个子模块组成的大模块叫做包，并把所有子模块放到同一个目录里。

在组成一个包的所有子模块中，需要优雅一个入口模块，入口模块的到处对象被称之为包的到处对象。

例如有如下目录结构, main.js作为入口模块

```
- /home/user/lib/
    - cat/
        head.js
        body.js
        main.js
```

其中定义了cat目录定义了一个包，有三个子模块

```
var head = require('./head');
var bdoy = require('./body');

exports.create = function (name) {
    return {
        name: name,
        head: head.create();
        body: body.create();
    };
};
```

使用`require('/home/user/lib/cat/main')` 能达到目的。

#### index.js

当文件的模块名是`index.js`，加载使用模块所在的目录的路径代替模块文件路径。

```
//以下两项等价
var cat = require('/home/user/lib/cat');
var cat = require('/home/user/lib/cat/index');
```

#### package.json

`package.json` 文件用于自定义入口模块的文件名和存放位置。cat模块可以重构如下：

目录结构

```
- /home/user/lib/
    - cat/
        + doc/
        - lib/
            head.js
            body.js
            main.js
        + tests/
        package.json
```

其中， package.json内容如下：

```
"name": "cat",
"main": "./lib/main.js"
```

这样就能通过`require('/home/user/lib/cat')`方式加载模块。

## 命令行程序

将写好的包或命令行程序导入系统的命令行程序。

#### Linux

- 文件顶部加入 #！ /usr/bin/env node
- 赋予执行权限 chmod +x /home/user/bin/node-echo.js
- 创建软链接 sudo ln -s /SRC_DIR /DES_DIR（绝对路径！）

 #### Windows

- 将文件所在路径加入环境变量
- 建立同名.cmd文件
- 内容 `@node "C:\User\user\bin\node-echo.js" %*`

## 工程目录

```
- /home/user/workspace/node-echo/ # 工程目录
    - bin/                                                    # 存放命令行相关代码
        node-echo                                       
    + doc/                                                  # 存放文档
    - lib/                                                     # 存放API相关代码
        echo.js
    - node_modules/                                # 存放三方包
        + argv/
    + tests/                                                # 存放测试用例
    package.json                                      # 存放元数据
    README.md                                       # 说明文件
```

```
/* bin/node-echo */
var argv = require('argv'),
    echo = require('../lib/echo');
    console.log(echo(argv.join(' ')));

/*  lib/echo.js */
modules.exportss = function (message) {
    return message;
};

/* package.json */
{
    "name": "node-echo",
    "main": "./lib/echo.js"
}
```
## NPM

- 允许用户从NPM服务器下载别人编写的三方包到本地使用。
- 允许用户从NPM服务器下载并安装别人编写的命令行程序到本地使用。
- 允许用户将自己编写的包或命令行程序上传到NPM服务器供别人使用。

#### 下载第三方包

单独安装，@可以加入版本号

`$ npm install argv@0.01`

批量安装，修改`package.json`

```
{
    "name": "node-echo",
    "main": "./lib/echo.js",
    "dependencies": {
        "argv" : "0.02"
    }    
}
```

#### 安装命令行程序
$ npm install node-echo `-g` 作用于全局系统

#### 发布代码

- 注册账号
- 填写`package.json`信息
- 在`package.json`所在目录运行`npm publish`

```
{
    "name" : "node-echo", #包名
    "version": "1.0.0", #版本号
    "dependencies": {
        "argv": "0.02"
    },
    "main": "./lib/echo.js" # 入口
    "bin": {
        "node-echo": "./bin/node-echo" # 命令行程序和主模块位置。
    }
}
```

#### 版本号X.Y.Z:

- X:大版本更新,向下不兼容
- Y:新功能,向下兼容
- Z:修复bug

#### 灵机一点

NPM 常用命令:

- NPM 最常用的 install,publish 和 可以查看help
- npm help <command> 查看某条命令的帮助
- 在` package.json`目录下使用 `npm install . -g`可以现在本地安装当前命令,可以用于发布前测试
- `npm update <package>`把`node_modules`子目录下的对应包更新
- `npm update <package> -g`可以把全局安装的对应命令升级至最新
- `npm cache clear`清空本地 npm缓存,用于对付使用相同版本号发布新代码的人
- `npm unpublish <package>@<version>`可以撤销发布自己发布过的某个版本

## 小结

本章介绍了编写 Nodejs 代码需要做的准备工作:

- 编写代码前先规划好目录结构
- 稍大写的程序可以将代码拆分成多个管理模块, 更大些的可以使用包来管理
- 合理使用`node_modules`和`NODE_PATH`来解耦包的使用方式和物理路径
- 使用NPM 加入 NodeJS生态圈互通有无
- 想到了心仪的包名时提前在 NPM 上抢注