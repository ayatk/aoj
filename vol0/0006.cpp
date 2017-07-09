#include <iostream>
#include <string>
using namespace std;

int main()
{
    string str;
    
    while (cin >> str)
    {
        int len = str.length();
        
        for (int i = len - 1 ; i >= 0; --i)
        {
            cout << str.at(i);
        }
        
        cout << "\n";
    }
    
    return 0;
}
