// copyright Google
// get_input2.cpp: Maggie Johnson
// Description: Illustrate the use of cin to get input
// and how to recover from errors.

#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
  int input_var = 0;
  do {
    cout << "Enter a number (-1 = quit): ";
    if (!(cin >> input_var)) {
      cout << "Please enter number only." << endl;
      cin.clear();
      cin.ignore(10000, '\n');
    }

    if (input_var != -1) {
      cout << "You entered! " << input_var << endl;
    }
  } while (input_var != -1);

  cout << "All done." << endl;
  return 0;
}
