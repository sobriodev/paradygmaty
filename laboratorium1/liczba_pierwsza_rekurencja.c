#include <stdio.h>

void prime(int n, int i);

int main(void) {
    int n;
    printf("Podaj liczbę naturalną, n = ");
    scanf("%d", &n);
    if (n < 1) {
        printf("%d nie jest liczbą pierwszą\n", n);
        return 0;
    }
    prime(n, 2);
    return 0;
}

void prime(int n, int i) {
    if (n == i) {
        printf("%d jest liczbą pierwszą\n", n);
        return;
    } else if (n % i == 0) {
        printf("Znaleziono podzielnik %d\n", i);
        return;
    } else {
        prime(n, ++i);
    }
}

