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

# Roman numbers problem

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         num = 0
#         for i in range(0, len(s)-1):
#             if roman[s[i]] < roman[s[i+1]]:
#                 num = num - roman[s[i]]
#             else:
#                 num = num + roman[s[i]]
#         return num + roman[s[-1]]   

# Longest prefix problem

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         minstr, maxstr = min(strs), max(strs)
#         i = 0
#         while i < len(minstr):
#             if minstr[i] != maxstr[i]:
#                 minstr = minstr[:i]
#             else:
#                 i += 1
#         return minstr            

# Valid Parenthesis

# class Solution:
#     def isValid(self, s: str) -> bool:
#         chars = {'(': ')', '{':'}','[':']'}
#         stack = []
#         for i in s:
#             if i in chars:
#                 stack.append(i)
#             elif stack == []:
#                 return False
#             elif i != chars[stack.pop()]:
#                 return False    
#         return stack == []  

# Remove duplicates
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 1
#         while i < len(nums):
#             if nums[i] == nums[i-1]:
#                 nums.pop(i)
#             else:
#                 i = i + 1 
#         return len(nums) 

# version 2 for remove duplicates

# x = 1
# for i in range(len(nums)-1):
# 	if(nums[i]!=nums[i+1]):
# 		nums[x] = nums[i+1]
# 		x+=1
# return(x)

#remove element

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         x = 0
      
#         for i in nums:
#             if i != val:
#                 nums[x] = i
#                 x += 1
              
#         return x 
       

# Index of the First Occurrence in a String

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle not in haystack:
#             return -1
#         else:
#             return len(haystack.split(needle)[0])    
     
# Search Insert Position
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         l = 0
#         u = len(nums) - 1
#         while l <= u:
#             mid = (l + u) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 u = mid - 1
#             else:
#                 l = mid + 1
#         return l  

# Length of Last Word
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         l = s.split()
   
#         if l:
#             return len(l[-1])
#         return 0    
                
# Plus one - my solution
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         array_str = [str(i) for i in digits]
#         array_join = int("".join(array_str))
#         sum = array_join + 1
#         return [int(j) for j in str(sum)]


# sqrt(x)
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x == 0:
#             return 0
#         low, high = 1, x
#         while low <= high:
#             mid = low + (high - low) // 2
#             if mid*mid == x:
#                 return mid
#             elif mid*mid < x:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return high  

# add binary
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         carry = 0
#         result = ''

#         a = list(a)
#         b = list(b)

#         while a or b or carry:
#             if a:
#                 carry += int(a.pop())
#             if b:
#                 carry += int(b.pop())

#             result += str(carry %2)
#             carry //= 2

#         return result[::-1]    


# Climbing stairs

# class Solution:
#     def climbStairs(self, n):
#         if n == 1:
#             return 1
#         res = [0 for i in range(n)]
#         res[0], res[1] = 1, 2
#         for i in range(2, n):
#             res[i] = res[i-1] + res[i-2]
#         return res[-1]

