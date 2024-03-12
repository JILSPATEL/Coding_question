"""

Problem Statement: Given an array, we have to find the average of all the elements in the array.

Examples:

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 3
Explanation: 
Average is the sum of all the elements divided by number of elements.
Therefore (1+2+3+4+5)/5 = 3.

Example 2:
Input:  N=6, array[] = {1,2,1,1,5,1}
Output: 1.8
Explanation: 
Average is the sum of all the elements divided by number of elements.
Therefore (1+2+1+1+5+1)/6 = 1.8

"""


def calculate_average_of_array(array, size):
    array_sum = 0
    for i in range(size):
        array_sum += array[i]

    average = round(array_sum / size, 1)
    return average


size = int(input("How many elements do you want to enter: "))
array = []
for i in range(size):
    element = int(input(f"Enter the {i+1} number: "))
    array.append(element)

print("Your input array is:", array)

print("Average of the array is:", calculate_average_of_array(array, size))
