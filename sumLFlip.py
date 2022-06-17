# Given a grid of array return the sum of reverse L version from top left to right bottom

# ex: 
# [[1,2],[1,1]] --> 4
# [1,3,1],[1,5,1],[4,2,1] --> 7

def sum_L_reverse(grid) -> int:
        total = sum(grid[0])
        for i in grid[1:]:
            total += i[len(i)-1]
        return total

print(sum_L_reverse([[1,3,1],[1,5,1],[4,2,1]]))
