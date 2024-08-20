# 3. Write a function that takes an array of numbers and sorts it in place, from smallest to largest.

def sort_in_place(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

array = [63,-2, 0, 113, 5, 77, -1]
sort_in_place(array)
print(array) 