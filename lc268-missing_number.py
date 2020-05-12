"""
  lc268-missing_number.py: Given an array containing n distinct 
  numbers taken from 0, 1, 2, ..., n, find the one that is missing 
  from the array.

  Example 1:
  Input: [3,0,1]
  Output: 2

  Example 2:
  Input: [9,6,4,2,3,5,7,0,1]
  Output: 8
  Note: Your algorithm should run in linear runtime complexity. Could 
  you implement it using only constant extra space complexity?
"""
import math
def main():
    test_list = [1]
    rtn_val = Solution.missingNumber(Solution(), test_list)
    print("Test List:", test_list)
    print("Missing Value:", rtn_val)

class Solution:
    def missingNumber(self, nums: list) -> int:
        sum = 0
        highest_val = 0
        for val in nums:
          sum += val
          if val > highest_val:
            highest_val = val
        if highest_val < len(nums): return len(nums)
        theory_val = (highest_val * (highest_val + 1)) // 2
        missing_val = theory_val - sum
        return missing_val

if __name__ == "__main__": main()