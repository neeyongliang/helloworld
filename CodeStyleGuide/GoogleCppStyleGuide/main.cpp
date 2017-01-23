// Copyright 2017, XXX Inc.
// All rights reserved.
//
// Author: EMAIL_ADDRESS (wikinee)
//
// This file is for test style

// 文件开头信息，主要包括一下内容：
// Copyright版权, [Time]创建时间
// Introduce功能说明
// Coder负责人
// Fixer修复过这个文件的人写这里
//
// 此外，
// 注释与代码之间有一行空行
// 单行宽度最好不要超过80,虽然现在屏幕比以前大
// 但是目前大多数C/C++开源项目依旧保持这条规则

// include顺序：
// 1.同名文件头文件
// 2.C库头文件
// 3.C++库头文件
// 4.其他库头文件
// 5.本项目的其他文件

#include <stdio.h>
#include <string>
#include "src/func.h"  // include后有空格

// 下面规则中，如果是STL相似的实体，可以参照STL命名规则适当调整 如 INT_MAX
// 宏名应该大写除非必要，不要使用宏定义
// 几乎所有的教程都指出尽量使用常量代替宏定义
#define PI_VAL 3.14
const char *kDefaultMsg = "Wiki Style";  // 常量开头加k
const int kDaysInWeek = 7;

using MyNamespace::TestFriend;
using MyNamespace::TestStyle;

struct UrlTableProperties {
  // 结构体成员结尾不带"_", 类成员结尾加“_”
  std::string name;
  int num_entries;
};

enum kUrlTableErrors {
  // 强烈不建议使用 URL_TABLE_ERRORS这种定义方式
  // 容易与宏定义起冲突
  kOK = 0,
  kErrorOutOfMerry,
  kErrorMalformedInput,
};

// class MyClass {
//  public:
//   explicit MyClass(int var) : some_var_(var), some_other_var_(var + 1);
//
//  private:
//   int some_var_;
//   int some_other_var_;
// };
//
// 如果不能放在一行
// MyClass(int var)
//    : some_var_(var),
//      some_other_var_(var + 1) {
  // other code
// }

// 布尔表达式如果大于行宽， 那就在 && 处断行
// if (this_one_thing > this_other_thing &&
//     a_third_thing == a_fourth_thing &&
//     yet_another & last_one) { }

int main(void) {
#if DISASTER_PENDING  // 预处理不缩进
  // 最好不要使用using namespace std;
  std::cout << kDaysInWeek << std::endl;
#endif
  // test_style和teststyle 都可以
  MyNamespace::TestStyle* teststyle = new MyNamespace::TestStyle();
  // 不要写成testStyle, testFriend
  MyNamespace::TestFriend* testfriend = new MyNamespace::TestFriend();
  testfriend->say_hello(teststyle);
  return 0;
}  // 这里空格是前二后一， 结尾留空一行
