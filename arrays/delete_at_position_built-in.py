# -----------------------------------------
# Program: Delete Element at Position
# Author: Soumajit Pal
# -----------------------------------------

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

pos = int(input("Enter position to delete: "))

if n == 0:
    print("Underflow")
elif pos < 0 or pos >= n:
    print("Invalid position")
else:
    arr.pop(pos)

print("Updated array:", arr)

"""
Time Complexity: O(n)
"""