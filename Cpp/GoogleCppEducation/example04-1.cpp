/*
 * Copyright [2017] create by wiki
 *
 */

#include<iostream>
#include<time.h>

using std::cout;
using std::endl;

int main() {
  int random_number;
  // Initialize random seed.
  srand (time(NULL));

  // Generate random number between 1 and 100
  random_number = rand() % 100 + 1;

  cout << "Your random number:" << random_number << endl;
  return 0;
}
