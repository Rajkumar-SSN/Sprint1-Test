# 2. Write a function that takes an array of numbers and returns a new array sorted from smallest to largest.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array = [63,-2, 0, 113, 5, 77, -1]
sorted_array = bubble_sort(array)
print(sorted_array)