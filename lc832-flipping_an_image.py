"""
lc832-flipping_an_image.py:
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:
Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

Notes:
1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
"""

class Solution:
    def flipAndInvertImage(self, A):
        for row_i in range(len(A)):
            row_len = len(A[row_i])
            for col_i in range(row_len//2):
                A[row_i][col_i], A[row_i][row_len-1-col_i] = A[row_i][row_len-1-col_i], A[row_i][col_i]
            for col_i in range(row_len):
                A[row_i][col_i] = int(not A[row_i][col_i])
        return A

def main():
    test_img = [[1,1,0,0,1],[1,0,0,1,1],[0,1,1,1,1],[1,0,1,0,1]]
    sln = Solution()
    print("Test Img:", test_img)
    rtn_img = sln.flipAndInvertImage(test_img)
    print("Result Img:", rtn_img)

if __name__ == "__main__":
    main()