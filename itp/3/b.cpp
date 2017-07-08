#include <iostream>
using namespace std;

int main()
{
    int x;
    int count = 0;
    
    while (cin >> x)
    {
        if (x == 0)
        {
            break;
        }
        
        cout << "Case " << ++count << ": " << x << endl;
    }
}
