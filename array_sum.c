#include <stdio.h>
#include <time.h>
int main(void) {
    int N ;
    printf("C言語における実行時間の検証");
    printf("Nの値を入力してください");
    scanf("%d", &N);
    long long  total = 0;
    clock_t start = clock();
    
    for (int i = 0; i < N; i++) {
        total += i;
    }

    clock_t end = clock();

     double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    
    printf("N: %d\n", N);
    printf("total: %lld\n", total);
    printf("elapsed: %f seconds\n", elapsed);
    return 0;
}
