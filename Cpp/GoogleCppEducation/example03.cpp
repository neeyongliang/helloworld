/*
 * Copyright [2017] create by wiki
 *
 */

#include <iostream>

using std::cout;
using std::endl;

int main(void) {
  cout << " 1\t2\t3\t4\t5\t6\t7\t8\t9" << endl << "" << endl;
  for (int c = 0; c < 10; c++) {
    cout << c << "| ";
    for (int i = 0; i < 10; i++) {
      cout << i * c << '\t';
    }
    cout << endl;
  }
  return 0;
}
