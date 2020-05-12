"""
lc242-valid_anagram.py: Given two strings s and t , write a function to determine 
if t is an anagram of s.

Example 1:
  Input: s = "anagram", t = "nagaram"
  Output: true
Example 2:
  Input: s = "rat", t = "car"
  Output: false
Note: You may assume the string contains only lowercase alphabets.
"""

def main():
    s = "anagram"
    t = "nagaram"
    bool_val = Solution.isAnagram(Solution(), s, t)
    print("Return Val:", bool_val)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_dict = {}
        for ch in s:
            val = cnt_dict.get(ch)
            if val is None:
                cnt_dict[ch] = 1
            else:
                cnt_dict[ch] += 1

        for ch in t:
            val = cnt_dict.get(ch)
            if val is None or val==0:
                return False
            else:
                if cnt_dict[ch] == 1:
                    del cnt_dict[ch]
                else:
                    cnt_dict[ch] -= 1
    
        return not bool(cnt_dict)        

if __name__ == "__main__":
    main()