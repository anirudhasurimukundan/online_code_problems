"""
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
"""

class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """

        """
        Logic: Rotate a matrix using a single line function [list(i) for i in zip(*mat)[::-1]] and compare to target matrix
        Note: one can rotate a matrix using the following one-line calls
                1. rotated = [list(i) for i in zip(*mat)][::-1] 
                2. rotated = list(zip(*mat))[::-1]
                3. rotated = list(reversed(list(zip(*mat))))
        """

        for rot in range(4):
            mat = [list(i) for i in zip(*mat)][::-1]
            #mat = list(reversed(list(zip(*mat))))
            if mat == target:
                return True
        return False

if __name__ == "__main__":

    sol = Solution;
    #mat = [[0,1],[1,0]]; target = [[1,0],[0,1]]
    #mat = [[0,1],[1,1]]; target = [[1,0],[0,1]]
    mat = [[0,0,0],[0,1,0],[1,1,1]]; target = [[1,1,1],[0,1,0],[0,0,0]]
    print(sol.findRotation(sol, mat, target))
