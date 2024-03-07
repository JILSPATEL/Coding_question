'''
Jack and Jill are playing a string game. Jack has given Jill two strings A and B. Jill has to derive a string C from A, by deleting elements from string A, such that string C does not contain any element of string B. Jill needs help to do this task. She wants a program to do this as she is lazy. Given strings A and B as input, give string C as Output.

Example 1:

Input:
tiger       -> input string A
ti          -> input string B
Output:
ger         -> Output string C

Explanation:
After removing “t” and “i” from “tiger”, we are left with “ger”.
So, the answer is “ger”.

Example 2:

Input:
processed           -> input string A
esd                 -> input string B
Output:
proc                -> Output string C

Explanation:
After removing “e” “s” and “d” from “processed”, we are left with “proc”.
So, the answer is “proc”.

'''


def findString(str1, str2):
    s1 = list(str1)
    s2 = list(str2)  # Convert to set for faster lookup
    result = []

    for char in s1:
        if char not in s2:
            result.append(char)

    return ''.join(result)


str1 = input("Enter String-1: ")
str2 = input("Enter String-2: ")
print("Output:", findString(str1, str2))
