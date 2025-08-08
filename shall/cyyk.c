// #include "kernel/syspub.h"
#include <stdio.h>
#include <stdlib.h>
float get_valid_float(const char *prompt)
{
    float value;
    while (1)
    {
        printf("%s", prompt);
        if (scanf("%f", &value) == 1)
        {
            while (getchar() != '\n')
                ; // 清除输入缓冲区
            return value;
        }
        else
        {
            printf("输入有误，请重新输入！\n");
            while (getchar() != '\n')
                ; // 清除输入缓冲区
        }
    }
}
int main()
{

    float result = 0;
    int op = 0;
    float x1 = 0;
    int flag = 0;
    printf("欢迎使用计算器！！\n");
    while (1)
    {
        if (flag == 0)
        {
            x1 = get_valid_float("请输入第一个数字：");
        }
        else
        {
            x1 = result;
        }
        printf("请选择你的操作！！\n");
        printf("1：加 2：减 3：乘 4：除 5：归零 0：退出");
        while (scanf("%d", &op) != 1 || op < 0 || op > 5)
        {
            printf("输入无效！ 请输入0-5的数字\n");
            // 清理缓冲区
            while (getchar() != '\n');
        }
        switch (op)
        {
        case 1:
            float x2 = get_valid_float("请输入第二个数字");
            result = x1 + x2;
            printf("结果是: %.2f\n", result);
            flag = 1;
            break;
        case 2:
            float x3 = get_valid_float("请输入第二个数字");
            result = x1 - x3;
            printf("结果是：%.2f\n", result);
            flag = 1;
            break;
        case 3:
            float x4 = get_valid_float("请输入第二个数字");
            result = x1 * x4;
            flag = 1;
            break;
        case 4:
            float x5 = get_valid_float("请输入第二个数字");
            if (x5 == 0)
            {
                printf("除数不能为0，请重新输入！\n");
                x5 = get_valid_float("");
            }
            result = x1 / x5;
            printf("结果是：%.2f\n", result);
            flag = 1;
            break;
        case 5:
            result = 0;
            printf("已将结果归零！\n");
            flag = 0;
            break;
        case 0:
            printf("退出计算器，感谢使用! \n");
            return 0;
            break;
        default:
            printf("功能选择错误,请重新输入");
            continue;
        }
    }
}
