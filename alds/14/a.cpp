#include <iostream>
using namespace std;

int main()
{
    string t, p;
    int c;
    cin >> t;
    cin >> p;
    
    if (t.length() < p.length()) {
        return 0;
    }
    
    for (size_t i = 0; i < t.length() - p.length() + 1; i++) {
        c = 0;
        
        for (size_t j = 0; j < p.length(); j++) {
            if (t[i + j] == p[j]) {
                c++;
            }
        }
        
        if (c == p.length()) {
            cout << i << endl;
        }
    }
    
    return 0;
}
