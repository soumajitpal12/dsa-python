n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

count = 0
total = 0

for num in arr:
    if num % 2 != 0:
        count += 1
        total += num

print("Count of odd numbers:", count)
print("Sum of odd numbers:", total)

"""
Time Complexity: O(n)
"""