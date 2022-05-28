class Solution:
    def missingNumber(nums):
        # pseudo code:
        #     for loop to iterate over 0 to len(num):
        #         return the number that is not in list
        
        for val in range(0,len(nums)+1):
            if val not in nums:
                return val

print(Solution.missingNumber([9,6,4,2,3,5,7,0,1]))