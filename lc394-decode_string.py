"""
lc394-decode_string.py
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4]. 

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""

class Solution:
    def decodeString(self, s: str) -> str:
        str_len = len(s)
        char_list = []
        i = 0
        while i < str_len:
            if s[i].isdigit():
                rtn_list, i = self.decode_bracket(s, i)
                char_list.extend(rtn_list)
            else:
                char_list.append(s[i])
                i += 1
        return "".join(char_list)

    def decode_bracket(self, msg, start_i):
        char_list, rtn_list = [], []
        repeat_size = 0
        cur_i = start_i
        while msg[cur_i].isdigit():
            cur_i += 1
        repeat_size = int(msg[start_i : cur_i])
        if msg[cur_i] != '[':
            raise Exception("Invalid format, expected opening backet!")
        cur_i += 1 # skip open bracket
        while msg[cur_i] != ']':
            if msg[cur_i].isdigit():
                rtn_list, cur_i = self.decode_bracket(msg, cur_i)
                char_list.extend(rtn_list)
            else:
                char_list.append(msg[cur_i])
                cur_i += 1
        cur_i += 1 # skip closing bracket
        rtn_list.clear()
        if repeat_size == 1:
            return char_list, cur_i
        for i in range(repeat_size):
            rtn_list.extend(char_list)
        return rtn_list, cur_i

def main():
    test_str = "3[a2[c]]"
    sln = Solution()
    print("Test String:", test_str)
    rtn_str = sln.decodeString(test_str)
    print("Return String:", rtn_str)

if __name__ == "__main__":
    main()