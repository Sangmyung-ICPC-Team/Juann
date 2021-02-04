int min(int a, int b)
{
    return (a < b) ? a : b;
}

int maxArea(int* height, int heightSize){
    int index = heightSize - 1;
    int container = 0;
    
    int op;
    
    for(int i = 0; i < heightSize; i++)
    {
        if(i >= index)
            break;
        op = min(height[i], height[index]) * (index - i);
        if(container < op)
            container = op;
        if(height[i] <= height[index])
            continue;
        else
        {
            index--;
            i--;
        }
    }
    return container;
}
