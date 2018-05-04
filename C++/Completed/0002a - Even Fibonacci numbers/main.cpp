#include <iostream>
using namespace std;

int fib_even_sum(int a, int b, int sum, int ceiling) {
    int c = a;
    a = b;
    b = b + c;
    if (a > ceiling)
        return sum;
    
    if (a % 2 == 0)
        fib_even_sum(a, b, sum+a, ceiling);
    else
        fib_even_sum(a, b, sum, ceiling);
}

int main() {
    printf("%d\n", fib_even_sum(1, 1, 0, 4000000));
}