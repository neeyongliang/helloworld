/*
 * Copyright [2017] create by wiki
 * file.cpp, Maggie Johnson
 * Description: An illustration of file processing
 */
#include <fstream>
#include <iostream>
using std::endl;
using std::cin;
using std::cout;
using std::ofstream;
using std::ios;
using std::ifstream;

int main() {
  char first_name[30], last_name[30];
  int age;
  char file_name[20];
  char done;

  cout << endl << "Enter the name of the file: ";
  cin >> file_name;
  // Create an ofstream called People, open the stream for output.
  ofstream People(file_name, ios::out);

  cout << endl << "Enter your data. " << endl;
  // Collect the data.
  while (1) {
    cout << "Enter First Name: ";
    cin >> first_name;
    cout << "Enter Last Name:  ";
    cin >> last_name;
    cout << "Enter Age:        ";
    cin >> age;
    // Write the output to the stream.
    People << first_name << endl << last_name << endl << age << endl;

    // Find out if they want to continue.
    cout << "Continue? y/n" << endl;
    cin >> done;
    if (done == 'n')
      break;
  }
  People.close();

  // Create an ifstream to read the file.
  ifstream People_in(file_name);

  while (1) {
    People_in >> first_name >> last_name >> age;
    if (People_in.eof())
      break;

    cout << endl << "First Name: " << first_name;
    cout << endl << "Last Name:  " << last_name;
    cout << endl << "Enter Age:  " << age;
    cout << endl;
  }
  People_in.close();
  return 0;
}
