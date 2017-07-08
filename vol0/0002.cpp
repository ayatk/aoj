#include <iostream>
#include <string>
using namespace std;

int main()
{
    int a, b;
    
    while (cin >> a >> b)
    {
        string str(to_string(a + b));
        cout << str.size() << endl;
    }
    
    return 0;
}
