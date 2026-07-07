"""
LeetCode Problem: 26. Remove Duplicates from Sorted Array
Difficulty: Easy

Problem:
Given a sorted array nums, remove the duplicates in-place such that
each unique element appears only once. Return the number of unique elements.

Time Complexity: O(n)
Space Complexity: O(1)

Author: Soumajit Pal
Repository: DSA_Python
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1


# -----------------------------
# Example (For Local Testing)
# -----------------------------
if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    sol = Solution()
    k = sol.removeDuplicates(nums)

    print("Number of unique elements:", k)
    print("Modified array:", nums[:k])