#include <stdio.h>

int main(void) {
    int numbers[5] = {1, 2, 3, 4, 5};
    int total = 0;

    for (int i = 0; i < 5; i++) {
        total += numbers[i];

        printf("numbers[%d] value: %d, address: %p\n",
               i, numbers[i], (void *)&numbers[i]);
    }

    printf("total: %d\n", total);

    return 0;
}
