/**
 * Copyright Google
 * get_input.cpp: Maggie Johnson
 * Description: Illustrate the use of cin to get input.
 */
#include <iostream>
using std::endl;
using std::cout;
using std::cin;

int main() {
  int input_var = 0;
  do {
    cout << "Enter a number (-1 = quit): ";
    if (!(cin >> input_var)) {
      cout << "You entered a non-numeric. Exiting..." << endl;
      break;
    }
    if (input_var != -1) {
      cout << "You enterd " << input_var << endl;
    }
  } while (input_var != -1);

  cout << "All done." << endl;
  return 0;
}
