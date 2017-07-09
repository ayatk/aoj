#include <iostream>
using namespace std;

int main()
{
    int n;
    
    while (cin >> n)
    {
        int debt = 100000;
        int rim = 0;
        
        for (int i = 0; i < n; ++i)
        {
            debt *= 1.05;
            
            if ((debt % 1000) != 0)
            {
                rim = 1000 - (debt % 1000);
            }
            
            debt += rim;
            rim = 0;
        }
        
        cout << debt << endl;
    }
    
    return 0;
}
