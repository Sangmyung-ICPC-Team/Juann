#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_SIZE 55

int num[MAX_SIZE]; //피연산자
char op[MAX_SIZE]; //연산자

int num_index = 0;
int op_index = 0;

void partition(char string[])
{
    char tmp[MAX_SIZE];
    int tmp_index = 0;
    int flag = 0;

    if(!isdigit(string[0])) //첫 문자가 op인 경우(-)
    {
        op[op_index++] = string[0];
        flag = 1;
    }
    else
        op[op_index++] = '+';

    int len = strlen(string);

    for(int i = 0 + flag; i < len; i++)
    {
        if(isdigit(string[i]))
            tmp[tmp_index++] = string[i];
        else
        {
            op[op_index++] = string[i]; //연산자 추가
            tmp[tmp_index] = '\0'; //피연산자 문자열 마무리
            num[num_index++] = atoi(tmp); //정수형으로 변경한 후 할당
            tmp_index = 0; //초기화
        }
    }
    tmp[tmp_index] = '\0';
    num[num_index++] = atoi(tmp); //마지막 피연산자 할당
}

int calculate()
{
    int sum = 0;

    ///(-)가 나올 때까지 (+)
    ///임시 변수 tmp
    int tmp = 0;

    for(int i = op_index - 1; i >= 0; i--)
    {
        if(op[i] == '-')
        {
            sum -= (num[i] + tmp);
            tmp = 0;
        }
        else
        {
            tmp += num[i];
        }
    }
    if(op[0] == '+')
        sum += tmp;

    return sum;
}

int main()
{
    char string[MAX_SIZE];
    scanf("%s", string);

    partition(string);
    printf("%d", calculate());

    return 0;
}
