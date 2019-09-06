#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

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

void mezcla(int arreglo[],int indices[])
{
    int i,j,k;
    int dimensionizq = indices[1] + 1;
    int dimensionder = indices[2] - indices[1];
    int izq[dimensionizq];
    int der[dimensionder];
    for(i = 0;i<dimensionizq;i++)
    {
        izq[i] = arreglo[indices[0]+i];
    }
    for(j = 0;j<dimensionder;j++)
    {
        der[j] = arreglo[indices[1]+1+j];
    }
    i = 0;
    j = 0;
    k = indices[0];
    while(i<dimensionizq && j<dimensionder)
    {
        if(izq[i]<=der[j])
        {
            arreglo[k] = izq[i];
            i++;
        }else
        {
            arreglo[k] = der[j];
            j++;
        }
        k++;
    }
    while(i<dimensionizq)
    {
        arreglo[k] = izq[i];
        i++;
        k++;
    }
    while(j<dimensionder)
    {
        arreglo[k] = der[j];
        j++;
        k++;
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
    int mitad = (longitudArreglo-1)/2;
    int indices [3];
   #pragma omp parallel sections
    {
        #pragma omp section
        qs(arreglo,0,mitad);
        #pragma omp section
        qs(arreglo,mitad+1,longitudArreglo-1);
    }
    indices [0] = 0;
    indices[1] = mitad;
    indices[2] = longitudArreglo-1;
    mezcla(arreglo,indices);
    for(int n =0;n<longitudArreglo;n++)
    {
        printf("%d ",arreglo[n]);
    }
}