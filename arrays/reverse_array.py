# -----------------------------------------
# Program: Reverse an Array
# Author: Soumajit Pal
# -----------------------------------------

def reverse_array(arr, n):
    left = 0
    right = n - 1

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

        left += 1
        right -= 1

    return arr


# MAIN
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = [0] * n

    for i in range(n):
        arr[i] = int(input(f"Enter element {i}: "))

    arr = reverse_array(arr, n)

    print("Reversed array:")
    for i in range(n):
        print(arr[i], end=" ")

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""