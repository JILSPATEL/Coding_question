'''

Given Two binary numbers (in 0 and 1) in the form of string. Find out whether there is a possibility whether these numbers can become equal by rearranging their respective Os and 1s.

For ex: 101 and 011 can be arranged within themselves to become either 101 or 011.

Example 1:

3   -> length of input string
101 -> input string 1
011 -> input string 2

output:
Yes

Example 2:

3   -> length of input string
111 -> input string 1
001 -> input string 2

output:
No

'''


def isBinaryString(list1, list2):

    str1 = list(list1)
    str2 = list(list2)

    str1Zero = 0
    str1One = 0

    str2Zero = 0
    str2One = 0
    if (len(str1) == len(str2)):
        for i in range(len(str1)):
            if (str1[i] == '1'):
                str1One += 1
            elif (str1[i] == '0'):
                str1Zero += 1
            if (str2[i] == '1'):
                str2One += 1
            elif (str2[i] == '0'):
                str2Zero += 1

    else:
        return "No"

    if (str1Zero != str2Zero):
        return "No"
    else:
        return "Yes"


str1 = input("Enter String-1 :")
str2 = input("Enter String-2 :")
print(isBinaryString(str1, str2))
