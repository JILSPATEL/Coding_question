"""

Problem Statement: Search an element in an array and return its position

Examples:

Example 1:
Input: array[] = {1,2,3,4,5} k=3                                                       0.                       
Output: 2                                                                                                              
             Explanation: The answer is 2 because 3 is present at 2nd index.

Example 2:
Input: array[]={6,7,10,5,3,10} k=10
Output: 5
Explanation: The answer is 2 & 5 because 10 is present at 2nd & 5th index.


"""


def findElement(array, element, len1):
    arr = []
    if element in array:
        for i in range(len1):
            if array[i] == element:
                arr.append(i)
        return arr
    else:
        return "No Element Present"


size = int(input("How many elements do you want to enter: "))
array = []
for i in range(size):
    element = int(input(f"Enter the {i+1} number: "))
    array.append(element)
element = int(input("Enter the element which you want to find : "))
print("Your input array is:", array)
len1 = len(array)
print("Element", element, "found at index:", findElement(array, element, len1))
