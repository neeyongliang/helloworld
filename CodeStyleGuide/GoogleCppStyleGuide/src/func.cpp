// Copyright 2017, XXX Inc.
// All rights reserved.
//
// Author: EMAIL_ADDRESS (wikinee)
//
// This file is for test style

#include "func.h"

MyNamespace::TestStyle::TestStyle() {
  type_ = "Coding Style";
}

std::string MyNamespace::TestStyle::get_type() {
  std::cout << type_ << std::endl;
  return type_;
}

void MyNamespace::TestFriend::say_hello(MyNamespace::TestStyle* t) {
  t->get_type();
}
