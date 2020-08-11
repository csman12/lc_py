"""
lc75-sort_colors.py :
Given an array with n objects colored red, white or blue, sort them in-place so that objects of 
the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

import random

class Solution:
    def sortColors(self, nums):
        i_r = 0 # red index
        i_b = len(nums) - 1 # blue index
        i = 0 # iterative list index

        while i <= i_b:
            if nums[i] == 2:
                nums[i], nums[i_b] = nums[i_b], nums[i]
                i_b -= 1             
                continue
            elif nums[i] == 0:
                nums[i], nums[i_r] = nums[i_r], nums[i]
                i_r += 1
                i += 1
                continue
            else:
                i += 1
                

def main():
    #test_list = [2,0,2,1,1,0]
    sln = Solution()
    num_of_test_lists = 5
    max_test_list_len = 20
    test_lists = []
    for i in range(num_of_test_lists):
        test_lists.append(rnd_list_gen(random.randint(0,max_test_list_len)))

    for test_list in test_lists:
        print(f"Testing List: {test_list}")
        sln.sortColors(test_list)
        print(f"Result List: {test_list}")

def rnd_list_gen(list_len):
    new_list = [0]*(list_len)
    for i in range(list_len):
        new_list[i] = random.randint(0, 2)
    return new_list

if __name__ == '__main__':
    main()