#include <iostream>
using namespace std;

int main()
{
    int x, y, max, min;
    
    while (cin >> x >> y)
    {
        if (x == 0 && y == 0)
        {
            break;
        }
        
        if (x < y)
        {
            max = y;
            min = x;
        }
        else
        {
            max = x;
            min = y;
        }
        
        cout << min << " " << max << endl;
    }
}
