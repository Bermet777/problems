# Two-sum problem June 6th 2023

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#       seen = {}
#       for i, num in enumerate(nums):
#           complement = target - nums[i]
#           if complement in seen:
#               return [i, seen[complement]]
#           else:
#               seen[num] = i 

# Palindrome number problem

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         initial = x
#         reversed = 0
#         while x > 0:
#             reversed = (reversed * 10) + x % 10
#             x = x//10
#         return initial == reversed 