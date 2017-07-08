#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int h, w;
    
    while (cin >> h >> w)
    {
        if (h == 0 && w == 0)
        {
            break;
        }
        
        for (int i = 0; i < h; i++)
        {
            if (i % 2 == 0)
            {
                for (int j = 0; j < w; ++j)
                {
                    cout << ((j % 2 == 0) ? "#" : ".");
                }
            }
            else
            {
                for (int j = 0; j < w; ++j)
                {
                    cout << ((j % 2 == 0) ? "." : "#");
                }
            }
            
            printf("\n");
        }
        
        printf("\n");
    }
}