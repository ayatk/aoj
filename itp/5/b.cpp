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
            if (0 == i || i == h - 1)
            {
                for (int j = 0; j < w; ++j)
                {
                    printf("#");
                }
            }
            else
            {
                printf("#");
                
                for (int j = 0; j < w - 2; ++j)
                {
                    printf(".");
                }
                
                printf("#");
            }
            
            printf("\n");
        }
        
        printf("\n");
    }
}