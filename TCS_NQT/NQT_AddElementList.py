n = int(input("Size of List is: "))
j = 0
List = [0 for i in range(n)]
for i in range(n):
    a = int(input(f"Number- {i+1} is: "))
    if a != 0:
        List[j] = a
        j += 1

print(List)
