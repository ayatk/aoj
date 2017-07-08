#include <iostream>
#include <algorithm>
#include <string>
#include <cctype>
using namespace std;

int main()
{
    int n, num;
    string card;
    cin >> n;
    int s[13] = {0}, h[13] = {0}, c[13] = {0}, d[13] = {0};
    
    for (int i = 0; i < n; i++)
    {
        cin >> card >> num;
        
        if (card == "S")
        {
            s[num - 1] = num;
        }
        else if (card == "H")
        {
            h[num - 1] = num;
        }
        else if (card == "C")
        {
            c[num - 1] = num;
        }
        else
        {
            d[num - 1] = num;
        }
    }
    
    for (int i = 0; i < 13; i++)
    {
        if (s[i] == 0)
        {
            cout << "S " << (i + 1) << endl;
        }
    }
    
    for (int i = 0; i < 13; i++)
    {
        if (h[i] == 0)
        {
            cout << "H " << (i + 1) << endl;
        }
    }
    
    for (int i = 0; i < 13; i++)
    {
        if (c[i] == 0)
        {
            cout << "C " << (i + 1) << endl;
        }
    }
    
    for (int i = 0; i < 13; i++)
    {
        if (d[i] == 0)
        {
            cout << "D " << (i + 1) << endl;
        }
    }
}