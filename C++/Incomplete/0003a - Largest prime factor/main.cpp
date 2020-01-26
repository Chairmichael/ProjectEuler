// main.cpp
// Project Euler Problem 3
// Largest Prime Factor

#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

// Largest Prime Factor
// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?

bool isPrime(unsigned long long);
vector<unsigned long long> primeFactorization(unsigned long long);

vector<unsigned long long> primeFactorization(unsigned long long n) {   
    vector<unsigned long long> factors;
    // Check for divisiblity by 2
    while (n % 2 == 0) {
        n = n / 2;
        factors.push_back(2);
    }
    unsigned long long d = 3; // divisor
    // while (n >= 1 || d < n) {
    while (!isPrime(n)) {
        // cout << "n = " << n << "\t" << "d = " << d << endl;
        if (n % d == 0 && isPrime(d)) {
            // cout << "Found factor = " << d << endl;
            factors.push_back(d);
            n = n / d;
        }
        else {
            do {
                d += 2;
            } while (!isPrime(d));
        }
    }
    factors.push_back(n);
    return factors;
}

// vector<unsigned long long> primeFactorization(unsigned long long n) {
//     vector<unsigned long long> factors;
//     unsigned long long x = floor(pow(n, 0.5));
//     if (x%2 == 0) x += 1;
//     for (unsigned long long d = 3; d <= x; d += 2) {
//         // cout << d << endl;
//         if (n % d == 0 && isPrime(d)) {
//             cout << d << endl;
//             factors.push_back(d);
//         }
//     }
//     return factors;
// }

bool isPrime(unsigned long long n) {
    if (n < 2) return false;
    else if (n == 2 || n == 3 || n == 5 || n == 7)
        return true;
    else if (n%2 == 0 || n%3 == 0 || n%5 == 0 || n%7 == 0)
        return false;
    else {
        for (unsigned long long d = 11; d < n / 2; d += 2) {
            if (n % d == 0)
                return false;
        }
        return true;
    }
}

int main() {
    unsigned long long num = 600851475143; // 13195
    vector<unsigned long long> primeFactors = primeFactorization(num);
    cout << endl << "Prime factors of " << num << ": ";
    for (auto const& factor: primeFactors)
        cout << factor << " ";
    cout << endl;
    // cout << "True = " << true << endl;
    // cout << "isPrime(377) == " << isPrime(377) << endl;
    // cout << "isPrime(1) == " << isPrime(1) << endl;
    // cout << "isPrime(7) == " << isPrime(7) << endl;
    // cout << "isPrime(11) == " << isPrime(11) << endl;
    // cout << "isPrime(257) == " << isPrime(257) << endl;
    // cout << "isPrime(100001) == " << isPrime(100001) << endl;
    // cout << "isPrime(100003) == " << isPrime(100003) << endl;
    return 0;
}
