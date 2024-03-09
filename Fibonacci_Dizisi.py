def fibonacci(n, cikti=[]):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
        cikti.append(str(a))
    return cikti

sayi = int(input("Fibonacci dizisinin uzunluğu: "))

print("Sonuç: {}".format(",".join(fibonacci(sayi))))
