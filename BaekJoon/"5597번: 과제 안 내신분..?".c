#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char * argv[]) {

    int numStudent[31][1] = {0};
    int num;
    for(int i = 1; i <= 28; i++)
    {
        scanf("%d", &num);
        numStudent[num][0] = 1;
    }
    
    for(int i = 1; i < 31; i++)
    {
        if(!numStudent[i][0])
            printf("%d\n", i);
    }
    
    
    retur
