
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
class Solution:
    def rotate(nums, k ):
        # brute force
        # for _ in range(k):
        #     last_num = nums.pop()
        #     nums.insert(0,last_num)
        
        k = k%len(nums)
        # inplace reverse the whole array
        l, r = 0 , len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1,  r - 1
        l,r = 0 , k-1
        # inplace reverse the part of the array from 0 index to k-1 index
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1,  r - 1
        l, r = k, len(nums)-1
        # inplace reverse the part of the array from k to len(nums)-1 index
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1,  r - 1