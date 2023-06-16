"""
https://leetcode.com/problems/rotate-image/
"""
class Solution(object):
    def rotate(self, matrix):
        """
        Logic: Interchange values in the outermost squares and then progress to inside squares
        Time complexity: O(n^2)
        Space complexity: O(1) since we do not use extra matrix or array
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1
        while l < r:
            t = l # assign top bound to (current) left bound
            b = r # assign bottom bound to (current) right bound -- determines whether we are in inside squares or outside squares
            for i in range(r-l):
                # store the top left element to a temporary variable
                topLeft = matrix[t][l+i]

                # bottom left to top left
                matrix[t][l+i] = matrix[b-i][l]

                # bottom right to bottom left
                matrix[b-i][l] = matrix[b][r-i]

                # top right to bottom right
                matrix[b][r-i] = matrix[t+i][r]

                # top left to top right
                matrix[t+i][r] = topLeft
            l += 1
            r -= 1

        return matrix

    def rotate_easy_code(self, matrix):
        """
        Logic: 1. Reverse the rows of the matrix; 2. Transpose this reversed row matrix to get the rotated matrix
        """
        l = 0
        r = len(matrix) - 1
        # Reverse the rows of the matrix
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # Transpose this reversed row matrix
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
            

if __name__ == "__main__":
    sol = Solution;
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print("Original matrix = ")
    for i in range(len(matrix)):
        print(matrix[i][:])
    print("Rotated matrix = ")
    rotated_matrix = sol.rotate_easy_code(sol, matrix)
    for i in range(len(matrix)):
        print(rotated_matrix[i][:])
 
