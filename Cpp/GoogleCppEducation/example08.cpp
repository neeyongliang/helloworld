/*
 * Copyright [2017] create by wiki
 * scope.cpp, Maggie Johnson
 * Description: A program to illustrate different scopes
 */

#include <iostream>

using std::cout;
using std::endl;

int a = 18;
int b = 6;

int function1(int a, int b) {
  cout << "a: " << a << " b: " << b << endl;
  return a - b; 
}

int function2() {
  int c;
  c = a + b;
  cout << "a: " << a << " b: " << b << endl;
  return c;
}

int main() {
  int b = 12;
  int c = 0;
  a = function1(b, a);
  c = function2();
  cout << "a: " << a << " b: " << b << " c: " << c << endl;
}
