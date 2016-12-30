/*
 * Copyright [2017] create by wiki
 * compensation.cpp, Maggie Johnson
 * Description: A program to decide the best of three methods of compensation
 */

#include <iostream>

using std::cout;
using std::endl;
using std::cin;

// constants which are used throughout the program
#define kPricePerUnit 225 // average price of a pair of shoes
#define kWeeklyWage 600   // current weekly wage - Method 1
#define kSalary 7.0       // hourly salary - Method 2
#define kHourcePerWeek 40 // number of houres worked - Method 2
#define kCommission2 0.10 // commission - Method 2
#define kCommission3 0.2  // commission - Method 3
#define kBonusPerUnit 20  // bonus - Method 3

// A function to get the weekly sales of units
int GetInput() {
  int units;
  cout << "Enter number of units sold per week: " << endl;

  if (!(cin >> units)) {
    cout << "Enter number of units sold per week: ";
    cout << "Numbers only" << endl;
  } else {
    return units;
  }
}

// This one is easy - always the same: $600 per week
void CalcMethod1() { cout << "Method 1: " << kWeeklyWage << endl; }

// Method 2: A salary of $7.00 per hour plus a 10% commission on sale
void CalcMethod2(int sales) {
  double PerHour, TotalPay, Commission;

  PerHour = kSalary * kHourcePerWeek;
  Commission = (sales * kPricePerUnit) * kCommission2;
  TotalPay = PerHour + Commission;
  cout << "Method 2: " << TotalPay << endl;
}

// Method 3: No salary, but 20% commissions and $20 for each pair of shoes sold
void CalcMethod3(int sales) {
  int Extra;
  double TotalPay, Commission;

  Extra = kBonusPerUnit * sales;
  Commission = (sales * kPricePerUnit) * kCommission3;
  TotalPay = Extra + Commission;
  cout << "Method 3: " << TotalPay << endl;
}

int main() {
  int WeeklySales;

  WeeklySales = GetInput();
  if (WeeklySales == 0) {
    return 0;
  }

  CalcMethod1();
  CalcMethod2(WeeklySales);
  CalcMethod3(WeeklySales);
}
