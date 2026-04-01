# -----------------------------------------
# Program: Insert Element at Position
# Author: Soumajit Pal
# -----------------------------------------

def insert_element(arr, n, max_size, pos, value):
    if n >= max_size:
        print("Overflow")
        return arr, n

    if pos < 0 or pos > n:
        print("Invalid position")
        return arr, n

    i = n - 1
    while i >= pos:
        arr[i + 1] = arr[i]
        i -= 1

    arr[pos] = value
    n += 1

    return arr, n


# MAIN
if __name__ == "__main__":
    max_size = int(input("Enter max size: "))
    n = int(input("Enter number of elements: "))

    arr = [0] * max_size

    for i in range(n):
        arr[i] = int(input(f"Enter element {i}: "))

    pos = int(input("Enter position: "))
    value = int(input("Enter value: "))

    arr, n = insert_element(arr, n, max_size, pos, value)

    print("Updated array:")
    for i in range(n):
        print(arr[i], end=" ")

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""