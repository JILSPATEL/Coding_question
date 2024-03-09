"""

Problem Statement: Find all the repeating elements present in an array.

Examples:

Example 1:
Input: 
Arr[] = [1,1,2,3,4,4,5,2]
Output:
 1,2,4
Explanation:
 1,2 and 4 are the elements which are occurring more than once.

Example 2:
Input:
 Arr[] = [1,1,0]
Output:
 1
Explanation:
 Only 1 is occurring more than once in the given array.

"""


def repeateEle(array):
    repeated_elements = []
    unique_elements = []

    for element in array:
        if element in unique_elements:
            repeated_elements.append(element)
        else:
            unique_elements.append(element)

    return sorted(repeated_elements)


size = int(input("How many elements do you want to enter: "))
array = []
for i in range(size):
    element = int(input(f"Enter the {i+1} number: "))
    array.append(element)

print("Your input array is:", array)
print("Repeating elements of the array are:", repeateEle(array))
