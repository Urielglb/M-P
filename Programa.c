#include <stdio.h>
int esPrimo(int n)
{
    for(int i=2;i<n;i++){
        if(n%i==0){
            return 0;
        }
    }
    return 1;
}
int main()
{
    int n;
    printf("Ingrese el número con el que desea trabajar\n");
    scanf("%d",&n);
    while(1<--n){
        int primo = esPrimo(n);
        if(primo==1){
            printf("%d es primo \n",n);
        }
    }
    return 0;
}
