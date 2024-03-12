""" 

Check if array is subset of another array.

Write a program to find whether an array is a subset of another array or not.

Given arr1[] and arr2[], we need to find whether arr1[] is a subset of arr2[]. An array is called a subset of another if all of its elements are present in the other array.

Note: Array elements are assumed to be unique.

Examples:

Example 1:
Input: arr1[]= [1,3,4,5,2]
       arr2[]= [2,4,3,1,7,5,15]
Output: arr1[] is a subset of arr2[]

Example 2:
Input: arr1[]= [1,3,4,5,2]
       arr2[]= [4,5,2]
Output: arr1[] is not a subset of arr2[]

Example 3:
Input: arr1[]= [1,3,4,5,2]
       arr2[]= [11,12,13,15,16]
Output: arr1[] is not a subset of arr2[]

"""


def isSubset(array1, array2):
    len1 = len(array1)
    len2 = len(array2)
    if len1 > len2:
        return False
    else:
        for i in range(len1):
            present = False
            for j in range(len2):
                if (array2[j] == array1[i]):
                    present = True
                    break
            if (present == False):
                return False
        return True


size1 = int(input("How many elements do you want to enter in sub Array: "))
size2 = int(input("How many elements do you want to enter in main Array: "))

print("--------Element of sub array--------")
array1 = []
for i in range(size1):
    element = int(input(f"Enter the {i+1} number: "))
    array1.append(element)
print("--------Element of main array--------")
array2 = []
for i in range(size2):
    element = int(input(f"Enter the {i+1} number: "))
    array2.append(element)

print("Your sub array is:", array1)
print("Your main array is:", array2)

if isSubset(array1, array2) == True:
    print("Array1 is Subset of Array2")
else:
    print("Array1 is Not Subset of Array2")
