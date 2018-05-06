#include <iostream>
#include <math.h>
using namespace std;
typedef unsigned long ulong;
// typedef unsigned double udouble;

// bool is_prime(ulong n) {
//     if (n == 2 || n == 3) return true;
//     if (n < 2 || n % 2 == 0) return false;
//     if (n < 9) return true;
//     if (n % 3 == 0) return false;
//     ulong r = (ulong)sqrt((double)n);
//     ulong f = 5;
//     while (f <= r) {
//         if (n % f == 0) return false;
//         if (n % (f+2) == 0) return false;
//         f += 6;
//     }
//     return true;
// }

bool is_prime(ulong n) {
    bool flag = true;
    for (int i = 2; i <= n / 2; i++) {
        if(n % i == 0) {
           flag = false;
           break;
        }
    }
    return flag;
}

// Largest prime factor
unsigned long lpf(ulong n) {
    // Get the square root to shorten the search
    ulong s = (ulong)sqrt((double)n) + 1;
    // Make sure s is odd
    if (s % 2 == 0) ++s;
    // Count down from the root by two
    for (ulong divisor = s; divisor > 3; divisor -= 2) {
        if (n % divisor == 0) {
            if (is_prime(n)) {
                return divisor;
            }
        }
    }
    return 0;
}

int main() {
    // unsigned long number = 600851475143;
    unsigned long number = 13195;
    // Largest prime factor
    printf("\n%d\n", lpf(number));
    // cout << "Largest prime factor of 600851475143: " << lpf(number) << endl;
    return 0;
}