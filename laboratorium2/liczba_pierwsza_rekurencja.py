def prime(n, i):
    if n == i:
        print("%d jest liczbą pierwszą" % n)
        return
    elif n % i == 0:
        print("Znaleziono dzielnik %d" % i)
        return
    else:
        prime(n, i + 1)


number = int(input("Podaj liczbę, n = "))
if number < 2:
    print("%d nie jest liczbą pierwszą" % number)
else:
    prime(number, 2)

