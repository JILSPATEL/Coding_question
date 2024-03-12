'''

Problem Statement: Given an array, we have to find the smallest element in the array.

Examples:

Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 0
Explanation: 
0 is the smallest element in the array. 

Example2: 
Input: arr[] = {8,10,5,7,9};
Output: 5
Explanation: 
5 is the smallest element in the array.

'''

# Method-1:


def smallest_number_of_array(array, size):
    sortedArray = sorted(array)
    temp = sortedArray[0]
    return temp


size = int(input("How many elements do you want to enter: "))
array = []
for i in range(size):
    element = int(input(f"Enter the {i+1} number: "))
    array.append(element)

print("Your input array is:", array)

print("Smallest of the array is:", smallest_number_of_array(array, size))


# Method-2:

def smallest_number_of_array(array, size):
    smallest = array[0]

    for i in array[1:]:
        if i < smallest:
            smallest = i
    return smallest


size = int(input("How many elements do you want to enter: "))
array = []
for i in range(size):
    element = int(input(f"Enter the {i+1} number: "))
    array.append(element)

print("Your input array is:", array)

print("Smallest of the array is:", smallest_number_of_array(array, size))
