/*
 * Copyright [2017] create by wiki
 * guess.cpp.  Maggie Johnson
 * Description: A guessing game where the player guesses
 * the secret number.
 */
#include<time.h>
#include<stdlib.h>
#include<iostream>


using std::cout;
using std::endl;
using std::cin;

int main(void) {
  int random_number, guess;
  // srand(time(NULL));
  unsigned int seed = time(NULL);
  // random_number = rand() % 100 + 1;
  random_number = rand_r(&seed) % 100 + 1;
  cout << random_number << endl;
  cout << "Guess out number (1 to 100): ";
  do {
    if (!(cin >> guess)) {
      cout << "Please enter only numbers." << endl;
    } else {
      if (random_number < guess) {
        cout << "The secret number is lower than " << guess << endl;
        cout << "Try again: ";
      } else if (random_number > guess) {
        cout << "The secret number is greater than " << guess << endl;
        cout << "Try again: ";
      } else {
        cout << "You guessed it: " << random_number << " is Right!" << endl;
        break;
      }
    }
  } while (guess != random_number);
  cout << "Congratulations!" <<  endl;
  return 0;
}
