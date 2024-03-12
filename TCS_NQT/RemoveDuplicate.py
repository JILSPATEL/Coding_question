def removeDup(array,len1):
    arr=[]
    for element in array:
        if element not in arr:
            arr.append(element)
    return arr

size = int(input("How many elements do you want to enter: "))
array1 = []
for i in range(size):
    element = int(input(f"Enter the {i+1} number: "))
    array1.append(element)
array=sorted(array1)
len1=len(array)
print("Your input array is:", array)
print("New Array is :",removeDup(array,len1))