'''

Alice has a very unique problem. He has a string which contain elements for 0 to 9. Find the number of substring of the string where sum of elements of the substring is not equal to the length of substring

Input 1:

-> length of string :3
-> string :201

Output 1:
2

'''


def noOfSubstring(strLen, str1):
    # s1=set(str1)
    count = 0
    sum = 0
    len1 = len(str1)
    for i in range(len1):
        sum += int(str1[i])
        if (sum <= strLen):
            count += 1
    return count


strLen = int(input("Enter The Length Of String :"))
str1 = input("Enter The String :")
print(noOfSubstring(strLen, str1))

# def noOfSubstring(strLen, str1):
#     count = 0
#     len1 = len(str1)
#     for i in range(len1):
#         sum = 0
#         for j in range(i, len1):
#             sum += int(str1[j])
#             if sum != j - i + 1:
#                 count += 1
#     return count

# strLen = int(input("Enter The Length Of String: "))
# str1 = input("Enter The String: ")
# print(noOfSubstring(strLen, str1))