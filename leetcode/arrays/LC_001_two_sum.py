"""
LeetCode Problem: 1. Two Sum
Difficulty: Easy

Problem:
Given an array of integers nums and an integer target,
return the indices of the two numbers such that they add up to target.

Time Complexity: O(n)
Space Complexity: O(n)

Author: Soumajit Pal
Repository: DSA_Python
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]

            seen[num] = i


# -----------------------------
# Example (For Local Testing)
# -----------------------------
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    sol = Solution()
    print(sol.twoSum(nums, target))