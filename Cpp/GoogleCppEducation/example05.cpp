/*
 * Copyright [2017] create by wiki
 * animal.cpp.  Maggie Johnson
 * Description: Computes combinations of animals under constraints
 * Horses cost $10, pigs cost $3, and rabbits are only $0.50. A farmer buys 100
 * animals for $100, How many of each animal did he buy?
 */

#include <iostream>

using std::cout;
using std::endl;

int main(void) {
  int h, p, r;
  for (h = 0; h < 11; h++) {
    for (p = 0; p < 34; p++) {
      for (r = 0; r < 101; r++) {
        if (h + p + r == 100) {
          if (((h * 10) + (p * 3) + (r * 0.5)) == 100) {
            cout << "Found one!" << h << " horses, " << p << " pigs, " << r
                 << " ribit" << endl;
          }
        }
      }
    }
  }
  return 0;
}
