#include "Palindrome.h"

// palindrome 回文，正反读取结果相同的意思。

bool Palindrome::isPalindrome(const std::string& toCheck)
{
    // try reverse string to compare origin string
    if (toCheck == std::string(toCheck.rbegin(), toCheck.rend())) {
        return true;
    }

    return false;
}