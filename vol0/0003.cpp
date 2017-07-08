#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
    int p[3] , n;
    
    while (cin >> n)
    {
        for (int i = 0; i < n; ++i)
        {
            cin >> p[0] >> p[1] >> p[2];
            sort(p, p + 3);
            cout << ((hypot(p[0], p[1]) == p[2]) ? "YES" : "NO") << endl;
        }
    }
}
