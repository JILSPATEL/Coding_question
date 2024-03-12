num = int(input("Enter the number: "))
reverse_num = 0
temp_num = num

while temp_num > 0:
    digit = temp_num % 10
    reverse_num = reverse_num * 10 + digit
    temp_num //= 10

if reverse_num == num:
    print("Palindrome")
else:
    print("Not Palindrome")
