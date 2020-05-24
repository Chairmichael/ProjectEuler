#include <iostream>
#include <climits>
#include <vector>
#include <math.h>
#include <chrono>
using namespace std;

// Largest Prime Factor
// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?

typedef unsigned long long int ullong;
bool isPrime(ullong);
ullong largest_prime_factor(ullong);
vector<ullong> prime_factors(ullong);

ullong largest_prime_factor(ullong n) {
    ullong ceiling = sqrt(n);
    if (ceiling % 2 == 0) ceiling++; 
    for (ullong divisor = ceiling; divisor > 2; divisor -= 2) {
        if (n % divisor == 0 && isPrime(divisor))
            return divisor;
    }
    return n;
}

vector<ullong> prime_factors(ullong n) {
    vector<ullong> factors;
    while (n % 2 == 0) {
        n /= 2;
        factors.push_back(2);
    }
    ullong ceiling = sqrt(n);
    if (ceiling % 2 != 0) ceiling++;
    for (ullong divisor = 3; divisor < ceiling; divisor += 2) {
        if (isPrime(divisor)) {
            while (n % divisor == 0) {
                n /= divisor;
                factors.push_back(divisor);
            }
        }
    }
    return factors;
}

bool isPrime(ullong n) {
    if (n <= 3) return true;

    const int DIVS_LENGTH = 4;
    ullong divisors[DIVS_LENGTH] = {2, 3, 5, 7};

    for (int i = 0; i < DIVS_LENGTH; i++) {
        if (n % divisors[i] == 0)
            return false;
    }

    ullong ceiling = sqrt(n);
    if (ceiling % 2 != 0) ceiling++;
    for (ullong d = 11; d < ceiling; d += 2) {
        if (n % d == 0) return false;
    }

    return true;
}

int main() {
    ullong number = 600851475143;

    chrono::steady_clock::time_point _start(chrono::steady_clock::now());

    largest_prime_factor(number);

    chrono::steady_clock::time_point _end(chrono::steady_clock::now());

    cout << chrono::duration_cast<chrono::duration<double>>(
                _end - _start).count() << " s" << endl;

    // for (auto i = factors.begin(); i != factors.end(); ++i) {
    //     cout << *i << " ";
    // }
    // cout << endl;
}
