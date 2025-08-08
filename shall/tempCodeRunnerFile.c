// #include "kernel/syspub.h" 
#include <stdio.h>
int main(){

    int result = 0;
    int op=0;
    int x1=0;
    int flag=0;
    printf("欢迎使用计算器！！\n");
    while(1){
        
        if(flag==0){
            printf("请输入第一个数字：");
            scanf("%d",&x1);
        }
        else{
            x1 = result;
        }
        printf("请选择你的操作！！\n");
        printf("1:加  2：减 3：乘  4：除  0：退出");
        scanf("%d",&op);
        switch(op)
        {
            case 1:
                printf("请输入第二个数字：");
                int x2=0;
                scanf("%d",&x2);
                result = x1 + x2;
                printf("结果是：%d\n",result);
                flag=1;
                break;
            case 2:
                printf("请输入第二个数字：");
                int x3=0;
                scanf("%d",&x3);
                result = x1 - x3;
                printf("结果是：%d\n",result);
                flag=1;
                break;
            case 3:
                printf("请输入第二个数字：");      
                int x4=0;
                scanf("%d",&x4);
                result = x1 * x4;
                printf("结果是：%d\n",result);
                flag=1;
                break;
            case 4:
                printf("请输入第二个数字：");
                int x5=0;
                scanf("%d",&x5);
                if(x5==0){
                    printf("除数不能为0，请重新输入！\n");
                    continue;
                }
                result = x1 / x5;
                printf("结果是：%d\n",result);
                flag=1;
                break;
            case 0:
                printf("退出计算器，感谢使用！\n");
                return 0;                    
        }
    
    }

}
