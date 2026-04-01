# -----------------------------------------
# Program: Count and Sum of Odd Numbers
# Author: Soumajit Pal
# -----------------------------------------

def odd_count_sum(arr, n):
    count = 0
    total = 0

    i = 0
    while i < n:
        if arr[i] % 2 != 0:
            count += 1
            total += arr[i]
        i += 1

    return count, total


# MAIN
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = [0] * n

    for i in range(n):
        arr[i] = int(input(f"Enter element {i}: "))

    count, total = odd_count_sum(arr, n)

    print("Count of odd numbers:", count)
    print("Sum of odd numbers:", total)

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""