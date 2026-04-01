# -----------------------------------------
# Program: Frequency Count of Elements
# Author: Soumajit Pal
# -----------------------------------------

def frequency_count(arr, n):
    visited = [0] * n

    for i in range(n):
        if visited[i] == 1:
            continue

        count = 1
        j = i + 1

        while j < n:
            if arr[i] == arr[j]:
                count += 1
                visited[j] = 1
            j += 1

        print(arr[i], "->", count)


# MAIN
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = [0] * n

    for i in range(n):
        arr[i] = int(input(f"Enter element {i}: "))

    frequency_count(arr, n)

"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""