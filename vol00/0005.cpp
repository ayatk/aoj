#include <iostream>
using namespace std;

int gcd(int m, int n)
{
    if ((0 == m) || (0 == n))
    {
        return 0;
    }
    
    while (m != n)
    {
        if (m > n)
        {
            m = m - n;
        }
        else
        {
            n = n - m;
        }
    }
    
    return m;
}

int lcm(int m, int n)
{
    if ((0 == m) || (0 == n))
    {
        return 0;
    }
    
    return ((m / gcd(m, n)) * n);
}

int main()
{
    int a, b;
    
    while (cin >> a >> b)
    {
        cout << gcd(a, b) << " " << lcm(a, b) << endl;
    }
    
    return 0;
}
