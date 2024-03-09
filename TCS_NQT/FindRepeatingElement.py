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


Problem Statement: Find all the non-repeating elements for a given array. Outputs can be in any order.

Examples:

Example 1:
Input:
 Nums = [1,2,-1,1,3,1]
Output:
 2,-1,3
Explanation:
 1 is the only element in the given array which occurs thrice in the array. -1,2,3 occurs only once and hence, these are non-repeating elements of the given array.

Example 2:
Input:
 Nums = [1,2,3]
Output:
 1,2,3
Explanation:
 All elements present in the array occur once. Hence, every element is non-repeating.
"""


def find_repeating_elements(array):
    repeating_elements = []
    unique_elements = []

    for element in array:
        if element in unique_elements:
            repeating_elements.append(element)
        else:
            unique_elements.append(element)
    
    all_elements = set(array)
    repeating_set = set(repeating_elements)
    non_repeating_set = all_elements - repeating_set
    
    print("Repeating elements of the array are:", sorted(list(repeating_set)))
    print("Non-repeating elements of the array are:", sorted(list(non_repeating_set)))

size = int(input("How many elements do you want to enter: "))
array = []
for i in range(size):
    element = int(input(f"Enter the {i+1} number: "))
    array.append(element)

print("Your input array is:", array)
find_repeating_elements(array)
