"""
  lc344-reverse_string.py: Write a function that reverses a string. 
  The input string is given as an array of characters char[].
  Do not allocate extra space for another array, you must do this by 
  modifying the input array in-place with O(1) extra memory.
  You may assume all the characters consist of printable ascii characters.

  Example 1:
  Input: ["h","e","l","l","o"]
  Output: ["o","l","l","e","h"]
  
  Example 2:
  Input: ["H","a","n","n","a","h"]
  Output: ["h","a","n","n","a","H"]
"""

def main():
    test_string = list("1234 String 5678")
    print("Starting String:", test_string)
    Solution.reverseString(Solution(), test_string)
    print("Reversed String:", test_string)

class Solution:
    def reverseString(self, s: list) -> None:
        # Note: Do not return anything, modify s in-place instead.
        if not list: return
        size = len(s)
        for i in range(size//2):
            tmp = s[i]
            s[i] = s[size-i-1]
            s[size-i-1] = tmp

if __name__ == "__main__": main()