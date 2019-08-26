#include <stdio.h>
#include <stdlib.h>

void swap(int arreglo[],int i, int j)
{
    int aux = arreglo[i];
    arreglo[i] = arreglo[j];
    arreglo[j] = aux;
}

void pivote(int arreglo[],int ini ,int fin)
{
    int random = (rand() % (fin - ini + 1)) + ini;
    swap(arreglo,random,fin);
}

int particion(int arreglo[],int ini ,int fin)
{
   pivote(arreglo,ini,fin);
   int piv = arreglo[fin];
   int i = ini-1;
   for(int j = ini;j<= fin-1;j++)
   {
       if(arreglo[j]<=piv)
       {
           swap(arreglo,++i,j);
       }
   }
   swap(arreglo,(i+1),fin);
   return(i+1);

}

void qs(int arreglo[],int ini,int fin)
{
    if(ini>=fin)
    {
        return ;
    }else
    {
        int part = particion(arreglo,ini,fin);
        qs(arreglo,ini,part-1);
        qs(arreglo,part+1,fin);
        
    }
    
}

int main ()
{
    int longitudArreglo ;
    scanf("%d",&longitudArreglo);
    int arreglo [longitudArreglo];
    for(int n =0;n<longitudArreglo;n++)
    {
        scanf("%d",&arreglo[n]);
    }
    qs(arreglo,0,longitudArreglo-1);
    for(int n =0;n<longitudArreglo;n++)
    {
        printf("%d ",arreglo[n]);
    }
}