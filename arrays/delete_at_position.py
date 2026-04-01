# -----------------------------------------
# Program: Delete Element at Position
# Author: Soumajit Pal
# -----------------------------------------

def delete_element(arr, n, pos):
    if n == 0:
        print("Underflow")
        return arr, n

    if pos < 0 or pos >= n:
        print("Invalid position")
        return arr, n

    i = pos
    while i < n - 1:
        arr[i] = arr[i + 1]
        i += 1

    n -= 1
    return arr, n


# MAIN
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = [0] * 100

    for i in range(n):
        arr[i] = int(input(f"Enter element {i}: "))

    pos = int(input("Enter position to delete: "))

    arr, n = delete_element(arr, n, pos)

    print("Updated array:")
    for i in range(n):
        print(arr[i], end=" ")

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""