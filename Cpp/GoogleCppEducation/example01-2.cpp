// hello3.cpp: copyright Maggie Johnson
// Description: a program that prints the immortal saying "hello world"
// many times and illustrates some cout flags

#include <iostream>
#include <iomanip>
using std::cout;
using std::endl;
using std::ios;

int main() {
  // set up cout to right-align
  cout << setiosflags(ios::left);
  // the first for loop will handle the rows
  for (int i = 0; i < 6; i++) {
    // the second for loop will handle the columns
    for (int j = 0; j < 4; j++) {
      // setw(int) sets the column width
      cout << std::setw(17) << "Hello World";
      // this next line is a part of the first for loop
      // and cause the new line
      cout << endl;
    }
    return 0;
  }
}
