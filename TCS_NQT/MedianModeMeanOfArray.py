from collections import Counter


def calculate_median(array, length):

    mid = int(length / 2)
    if length % 2 == 0:
        median = round(float((array[mid - 1] + array[mid]) / 2), 1)
    else:
        median = array[mid]
    return median


def calculate_mode(array, length):

    counts = Counter(array)
    # Find the maximum occurrence
    max_occurrence = max(counts.values())
    # Find the mode(s) (numbers with maximum occurrence)
    modes = []
    for key, value in counts.items():
        if value == max_occurrence:
            modes.append(key)
    return modes


def calculate_mean(array, length):

    total_sum = 0
    for i in range(length):
        total_sum += array[i]
    mean = round(float(total_sum / length), 1)
    return mean


input_choice = input("What do you want to find (MEAN/MODE/MEDIAN) : ").lower()
size = int(input("How many elements do you want to enter: "))
input_array = []
for i in range(size):
    element = int(input(f"Enter the {i+1} number: "))
    input_array.append(element)

print("Your input array is:", input_array)
sorted_array = sorted(input_array)
print("Sorted input array is:", sorted_array)
array_length = len(sorted_array)

if input_choice == "median":
    print("Median of array :", calculate_median(sorted_array, array_length))

elif input_choice == "mode":
    print("Mode Value of Array :", calculate_mode(sorted_array, array_length))

elif input_choice == "mean":
    print("Mean of Array :", calculate_mean(sorted_array, array_length))


"""

Here's the updated description with examples for all three modes (mean, median, and mode):

Description:
This Python script provides functionalities to calculate the mean, mode, and median of a given list of numbers. It uses the `calculate_mean`, `calculate_mode`, and `calculate_median` functions to compute these statistics. The script prompts the user to choose which statistic they want to calculate and input the list of numbers. It then displays the input list, sorts it, calculates the chosen statistic, and prints the result.

Input:
- The user is prompted to choose which statistic to calculate (mean, mode, or median).
- The user is prompted to enter the number of elements in the list.
- The user is asked to input the elements of the list one by one.

Output:
- The input array provided by the user.
- The sorted input array.
- The calculated statistic based on the user's choice (mean, mode, or median).

Example (Mean):

What do you want to find (MEAN/MODE/MEDIAN) : mean
How many elements do you want to enter: 4
Enter the 1 number: 10
Enter the 2 number: 20
Enter the 3 number: 30
Enter the 4 number: 40
Your input array is: [10, 20, 30, 40]
Sorted input array is: [10, 20, 30, 40]
Mean of Array : 25.0

Example (Median):

What do you want to find (MEAN/MODE/MEDIAN) : median
How many elements do you want to enter: 5
Enter the 1 number: 12
Enter the 2 number: 7
Enter the 3 number: 9
Enter the 4 number: 15
Enter the 5 number: 4
Your input array is: [12, 7, 9, 15, 4]
Sorted input array is: [4, 7, 9, 12, 15]
Median of array : 9.0

Example (Mode):

What do you want to find (MEAN/MODE/MEDIAN) : mode
How many elements do you want to enter: 6
Enter the 1 number: 3
Enter the 2 number: 4
Enter the 3 number: 5
Enter the 4 number: 5
Enter the 5 number: 6
Enter the 6 number: 6
Your input array is: [3, 4, 5, 5, 6, 6]
Sorted input array is: [3, 4, 5, 5, 6, 6]
Mode of Array : [5, 6]


"""
