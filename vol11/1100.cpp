#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int n;
    int count = 0;

    while (cin >> n) {
        if (n == 0) {
            break;
        }

        int x[n], y[n];

        for (int i = 0; i < n; ++i) {
            cin >> x[i] >> y[i];
        }

        float pol = 0;

        for (int k = 0; k < n - 1; k++) {
            pol += x[k] * y[k + 1] - x[k + 1] * y[k];
        }

        pol += x[n - 1] * y[0] - x[0] * y[n - 1];

        if (pol < 0) {
            pol *= -1;
        }

        printf("%d %#.1f\n", ++count, pol / 2);
    }
}
