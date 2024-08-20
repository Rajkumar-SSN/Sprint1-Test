# 4. Write a function that reverses an array in place.

def reverse_array_in_place(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


array = [63,-2, 0, 113, 5, 77, -1]
reverse_array_in_place(array)
print(array)