n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for key in freq:
    print(key, "->", freq[key])

"""
Time Complexity: O(n)
"""