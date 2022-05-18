from ctypes import pointer

from numpy import number


class Solution:
    def removeDuplicates(nums):
        #pseudo code:
        # use left and right pointer
        # left pointer only change by +1 when right pointer in the for loop check if the current number
        # and the previous numbers are not the same, return left pointer at the end to found out how many
        # unique numbers were in nums
        l=1
        for i in range(1,len(nums)):
            if nums[i] !=nums[i-1]:
                nums[l] = nums[i]
                l +=1
        return l

print(Solution.removeDuplicates([1,1,2]))