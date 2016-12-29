CMake Note
------

The CMake learning note for [CMake 入门实践](http://hahack.com/codes/cmake/)

#### 内容

- 单个文件

- 多个文件

- 自定义编译选项

- 支持gdb

- 添加环境检查

- 添加版本号

- 生成安装包


#### 将其他平台的项目迁移到 CMake

CMake 可以很轻松地构建出在适合各个平台执行的工程环境。而如果当前的工程环境不是 CMake ，而是基于某个特定的平台，是否可以迁移到 CMake 呢？答案是可能的。下面针对几个常用的平台，列出了它们对应的迁移方案。

#### autotools

  - am2cmake 可以将 autotools 系的项目转换到 CMake，这个工具的一个成功案例是 KDE 。

  - Alternative Automake2CMake 可以转换使用 automake 的 KDevelop 工程项目。

  - Converting autoconf tests

#### qmake

- qmake converter 可以转换使用 QT 的 qmake 的工程。

#### Visual Studio

  - vcproj2cmake.rb 可以根据 Visual Studio 的工程文件（后缀名是 .vcproj 或 .vcxproj）生成 CMakeLists.txt 文件。

  - vcproj2cmake.ps1 vcproj2cmake 的 PowerShell 版本。

  - folders4cmake 根据 Visual Studio 项目文件生成相应的 “source_group” 信息，这些信息可以很方便的在 CMake 脚本中使用。支持 Visual Studio 9/10 工程文件。

#### CMakeLists.txt 自动推导

  - gencmake 根据现有文件推导 CMakeLists.txt 文件。

  - CMakeListGenerator 应用一套文件和目录分析创建出完整的 CMakeLists.txt 文件。仅支持 Win32 平台。
