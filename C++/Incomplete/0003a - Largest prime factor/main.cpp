#include <iostream>
#include <math.h>
using namespace std;

bool is_prime(unsigned long n) {
    if (n == 2 || n == 3) return true;
    if (n < 2 || n % 2 == 0) return false;
    if (n < 9) return true;
    if (n % 3 == 0) return false;
    unsigned long r = (unsigned long)sqrt((double)n);
    unsigned long f = 5;
    while (f <= r) {
        if (n % f == 0) return false;
        if (n % (f+2) == 0) return false;
        f += 6;
    }
    return true;
}

// Largest prime factor
unsigned long lpf(unsigned long n) {
    // Get the square root to shorten the search
    // unsigned long s = (unsigned long)sqrt((double)n) + 1;
    unsigned long s = n / 2;
    // Make sure s is odd
    if (s % 2 == 0) s += 1;
    // Count down from the root by two
    for (unsigned long divisor = s; divisor >= 3; --divisor) {
        // printf("        %d\n", divisor);
        if (n % divisor == 0 && is_prime(divisor)) {
            return divisor;
        }
    }
    if (n % 2 == 0) {
        return 2;
    } else {
        return 1;
    }
}

int main() {
    unsigned long number = 600851475143;
    // unsigned long number = 13195;
    printf("%d: %d\n", number, lpf(number));
    // Largest prime factor
    // for (int i = 0; i < 100; ++i) {
    //     printf("%d: %d\n", i, lpf(i));
    // }
    // cout << "Largest prime factor of 600851475143: " << lpf(number) << endl;
    return 0;
}