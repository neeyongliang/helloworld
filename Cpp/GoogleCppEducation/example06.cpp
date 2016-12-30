/*
 * Copyright [2017] create by wiki
 * Help: http://www.yolinux.com/TUTORIALS/LinuxTutorialC++StringClass.html
 */

#include <iostream>

using std::cout;
using std::endl;
using std::string;

int main(void) {
  string str1 = "To be or not to be, that is the question";
  string str2 = "only ";
  string str3 = str1.substr(6, 12);
  str1.insert(32, str2);
  if (str1.find("to be", 22) == string::npos) {
    cout << "FIND FAILED!" << endl;
  }

  str1.replace(str1.find("to be", 0), 5, "to jump");
  str1.erase(9, 4);
  cout << str1 << endl;
  for (int i = 0; i < str3.length(); i++) {
    cout << str3[i];
    cout << endl;
  }

  return 0;
}
