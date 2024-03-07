n = int(input("Enter index: "))

a, b = 0, 0
for i in range(n):
    if (i % 2 != 0):
        a += 2
    else:
        b = a/2

if (n % 2 != 0):
    print(a)
else:
    print(b)
