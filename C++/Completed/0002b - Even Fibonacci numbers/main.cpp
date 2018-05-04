#include <iostream>
#include <vector>
using namespace std;

vector<int> fib(int ceiling) {
    vector<int> v = {1, 2};
    int le = v.size() - 1;
    printf("%d\n", le);
    while (v[le] < ceiling) {
        v.push_back(v[le] + v[le-1]);
    }
}

int main() {
    vector<int> v = fib(40);
    // int sum = 0;
    // for (auto e = v.cbegin(); e != v.cend(); e++)
    //     if (*e % 2 == 0)
    //         sum += *e;
}