num = int(input("Enter the number: "))
sum = 0
temp_num = num

while temp_num > 0:
    digit = temp_num % 10
    sum = sum + digit**3
    temp_num //= 10

if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")
