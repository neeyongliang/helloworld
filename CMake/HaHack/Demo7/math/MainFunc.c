//Function List

double power(double base, int exponent) {
  int result = (int)base;
  int i;

  if (exponent == 0) {
    return 1;
  }

  for (i = 1; i < exponent; ++i) {
    result = result * (int)base;
  }

  return result;
}