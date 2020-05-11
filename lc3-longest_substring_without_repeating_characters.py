"""
  lc3-longest_substring_without_repeating_characters.py: Given a string, 
  find the length of the longest substring without repeating characters.

  Example 1:
  Input: "abcabcbb"
  Output: 3 
  Explanation: The answer is "abc", with the length of 3. 
  
  Example 2:
  Input: "bbbbb"
  Output: 1
  Explanation: The answer is "b", with the length of 1.
  
  Example 3:
  Input: "pwwkew"
  Output: 3
  Explanation: The answer is "wke", with the length of 3. 
  Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def main():
    sln = Solution.lengthOfLongestSubstring(Solution(), "pwwkew")
    print("Longest Substring Size: ", sln)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sln_str = [0, 0] # (index, str_size)
        cur_str = [0, 0] # (index, str_size)
        ch_dict = {} # {key=char, value=index of char in string s}
        for i in range(len(s)):
            if ch_dict.get(s[i]) is not None: # if repeat char, then...
                # check cur_str with sln_str and update if cur_str is bigger
                if cur_str[1] > sln_str[1]: sln_str[0],sln_str[1] = cur_str[0],cur_str[1]
                # delete keys for chars of slice cur_str beginning index to location of first repeat char
                for ch in s[cur_str[0]:(ch_dict.get(s[i]))] : del ch_dict[ch]
                # set cur_str with index of first repeat char and size of current index minus location of first repeat char
                cur_str[0] = ch_dict[s[i]] + 1  # update index of cur_str
                cur_str[1] = i - ch_dict[s[i]]  # update char size of cur_str
                # update the location of the repeat char in the dictionary
                ch_dict[s[i]] = i

            # else add current char to dict and increment cur_str size
            else:
                ch_dict[s[i]] = i
                cur_str[1] += 1

        # check if the last cur_str is bigger than sln_str and update sln_str if so
        if cur_str[1] > sln_str[1]: sln_str[0],sln_str[1] = cur_str[0],cur_str[1]

        #print("Solution Substring:", s[sln_str[0]:(sln_str[0]+sln_str[1])])
        return sln_str[1]
            
if __name__ == "__main__": main()