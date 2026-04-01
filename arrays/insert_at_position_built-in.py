n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

pos = int(input("Enter position: "))
value = int(input("Enter value to insert: "))

if pos < 0 or pos > n:
    print("Invalid position")
else:
    arr.insert(pos, value)

print("Updated array:", arr)

"""
Time Complexity: O(n)
"""