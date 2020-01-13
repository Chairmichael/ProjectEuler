#include <iostream>
#include <math.h>
using namespace std;

// Largest Prime Factor
// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?

bool isPrime(long n) {
    if (n < 2) return false;
    else if (n%2 == 0 || n%3 == 0 || n%5 == 0 || n%7 == 0)
        return false;
    else {
        for (int d = 11; d < n / 2; d += 11) {
            if (n % d == 0)
                return false;
        }
        return true;
    }
}

int main() {
    cout << "isPrime(12) == " << isPrime(12) << endl;
    cout << "isPrime(1) == " << isPrime(1) << endl;
    cout << "isPrime(257) == " << isPrime(257) << endl;
    cout << "isPrime(100001) == " << isPrime(100001) << endl;
    return 0;
}