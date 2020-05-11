"""
  lc7-reverse_integer.py: Given a 32-bit signed integer, 
  reverse digits of an integer.

  Example 1:
    Input: 123
    Output: 321
  Example 2:
    Input: -123
    Output: -321
  Example 3:
    Input: 120
    Output: 21
  Note: Assume we are dealing with an environment which could only store 
  integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For 
  the purpose of this problem, assume that your function returns 0 when 
  the reversed integer overflows.
"""

def main():
    result = Solution.reverse(Solution(),  8463847412)
    print("RESULT:", result)

class Solution:
    def reverse(self, x: int) -> int:
        rtn_val = 0
        neg_flag = False
        if x < -0:
            neg_flag = True
            x *= -1 
        while x > 0:
            digit = x % 10
            x = x // 10
            rtn_val = (rtn_val * 10) + digit
        if neg_flag:
            rtn_val = rtn_val * -1
        if rtn_val < -2147483648 or rtn_val > 2147483647: rtn_val = 0
        return rtn_val

if __name__ == "__main__":
    main()