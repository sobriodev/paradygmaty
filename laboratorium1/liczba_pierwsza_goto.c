#include <stdio.h>

int main(void) { 
    int n;
    printf("Podaj liczbę naturalną, n = ");
    scanf("%d", &n);

    if (n < 1) {
        printf("%d nie jest liczbą pierwszą\n", n);
        return 0;
    }

    int i = 2;
    calc:
    if (i == n) {
        printf("%d jest liczbą pierwszą\n", n);
        return 0;
    } else if (n % i == 0) {
        printf("Znaleziono podzielnik %d\n", i);
        return 0;
    }
    ++i;
    goto calc;
}

