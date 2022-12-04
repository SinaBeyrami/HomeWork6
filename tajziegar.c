#include <stdio.h>

int main(){

    int n;
    printf("Please enter the number: ");
    scanf ("%d" , &n);
    int m=n;
    printf("%d = " , n);
    for (int i=2 ; i*i<=m ; i++){
        int t=0;
        while (n%i == 0){
            n/=i;
            ++t;
        }
        if (t){
            printf("%d^%d" , i , t);
        }
        if (n != 1 && t!=0){
            printf(" * ");
        }
    }
    if (n != 1){
        printf("%d" , n);
    }
    return 0;
}
