"""

Problem Statement: You are given an array. The task is to reverse the array and print it. 

Examples:

Example 1:
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

Example 2:
Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

"""

"""

Certainly! `(size - 1, -1, -1)` represents the parameters passed to the `range()` function:

1. The first parameter `size - 1`: This specifies the starting point of the range. It starts from `size - 1` because array indexing in Python starts from 0, so the last index of the array is `size - 1`.
2. The second parameter `-1`: This specifies the end point of the range. It is -1 because we want to iterate till index 0 (inclusive). A step of -1 means the loop iterates backwards.
3. The third parameter `-1`: This specifies the step size of the range. It is -1 because we want to move backwards from the starting point towards the end point.

So, when we write `for i in range(size - 1, -1, -1)`, it means the loop will start from the last index of the array (`size - 1`), iterate till the first index (`-1`), and move backward by decrementing the index by `-1` each time.

"""


def revarray(array, size):
    revArray = []
    for i in range(size - 1, -1, -1):
        revArray.append(array[i])
    return revArray


size = int(input("How many elements do you want to enter: "))
array = []
for i in range(size):
    element = int(input(f"Enter the {i+1} number: "))
    array.append(element)

print("Your input array is:", array)

print("Reversed array:", revarray(array, size))
