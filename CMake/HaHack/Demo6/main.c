#include <stdio.h>
#include "config.h"
#ifdef USE_MYMATH
  #include "math/MainFunc.h"
#else
  #include <stdlib.h>
#endif
int main(int argc, char *argv[])
{
    if (argc < 3){
        printf("Usage: %s base exponent \n", argv[0]);
        return 1;
    }
    double base = atof(argv[1]);
    int exponent = atoi(argv[2]);
    
#ifdef HAVE_POW
    printf("Now we use our own Math library. \n");
    double result = power(base, exponent);
#else
    printf("Now we use the standard library. \n");
    double result = pow(base, exponent);
#endif
    printf("%f ^ %d is %f\n", base, exponent, result);
    return 0;
}