// Copyright 2017, XXX Inc.
// All rights reserved.
//
// Author: EMAIL_ADDRESS (wikinee)
//
// This file is for test style

#ifndef SRC_FUNC_H_  // <PATH_IN_PROJECT>_<FILE_BASE_NAME>_H_
#define SRC_FUNC_H_  // 此处需配合CPPLINT.cfg文件

#include <iostream>
#include <string>

namespace MyNamespace {  // 最外层的namespace内容里，上下各空一行。

// 多个namespace不缩进
class TestStyle {  // 类名的单词首字母全部要大写，是AbcDef不是abcDef!
friend void say_hello(TestStyle* t);  // friend集中写在类最开始

 public:  // 一个空格
  TestStyle();
  std::string get_type();
  // 函数与左括号之间没有空格,取值函数与设置函数，命名往往与参数有关
  // 特别短小或者内联的也可以使用小写字母

 private:
  std::string type_;  // 成员_结尾
};

class TestFriend {
 public:
  // 指针与引用左对齐或者右对齐都可以，但不能两边都空
  void say_hello(TestStyle* t);
};

}  // namespace MyNamespace
// 命名空间结束，需要注释说明

#endif  // SRC_FUNC_H_
