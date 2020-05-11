"""
// lc17-letter_combinations_phone_number.py
// Given a string containing digits from 2-9 inclusive, return all possible 
// letter combinations that the number could represent. A mapping of digit 
// to letters(just like on the telephone buttons) is given below. Note that 
// 1 does not map to any letters.

// number to character mapping
// 2 - abc
// 3 - def
// 4 - ghi
// 5 - jkl
// 6 - mno
// 7 - pqrs
// 8 - tuv
// 9 - wxyz

// Example:
//    Input: "23"
//    Output : ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
def main():
    result = Solution.letterCombinations(Solution(), "56")
    print("result: ", result)

class Solution:
    def letterCombinations(self, digits: str) -> list:
        num_to_alpha_list_map = {
            '1': None,
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        def list_repeat(r_list, cnt):
            if not r_list or not len(r_list): 
                r_list = []
                for i in range(cnt+1):
                    r_list.append([])
                return r_list
            repeat_size = len(r_list)
            for i in range(cnt):
                for ii in range(repeat_size):
                    r_list.append(r_list[ii].copy())
            return r_list

        sln = []
        for i in range(len(digits)):
            char_list = num_to_alpha_list_map.get(digits[i])
            if char_list: 
                sln = list_repeat(sln, len(char_list)-1)
                for ch in range(len(char_list)):
                    for ii in range(len(sln)//len(char_list)):
                        sln[ii+(ch*(len(sln)//len(char_list)))].append(char_list[ch])

        #convert to list of strings            
        str_sln = []
        for i in range(len(sln)):
            str_sln.append("".join(sln[i]))
        return str_sln

if __name__ == '__main__':
    main()