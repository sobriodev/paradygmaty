def smallest_divider(n, i):
    if n % i == 0:
        return i
    elif i * i >= n:
        return n
    else:
        return smallest_divider(n, i + 1)


n = int(input('Podaj liczbę naturalną, n = '))
i = smallest_divider(n, 2)
if n == i:
    print('{} jest liczbą pierwszą'.format(n))
else:
    print('Znaleziono podzielnik {}'.format(i))

