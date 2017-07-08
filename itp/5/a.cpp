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
        
        for (int i = 0; i < h; ++i)
        {
            for (int i = 0; i < w; ++i)
            {
                printf("#");
            }
            
            printf("\n");
        }
        
        printf("\n");
    }
}