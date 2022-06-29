# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

class Solution:
    def rotate(matrix):
        new_list = [[] for _ in range(len(matrix[0]))]

        i = 0
        while i<len(matrix[0]):
            for l in matrix:
                new_list[i].append(l[i])
            i += 1
        return [list(reversed(row)) for row in new_list]


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(Solution.rotate(matrix))