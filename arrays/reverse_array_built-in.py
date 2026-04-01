n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

arr.reverse()

print("Reversed:", arr)

"""
Time Complexity: O(n)
"""