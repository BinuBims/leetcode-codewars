class Solution(object):
    def longestConsecutive(nums):
        # pseudo code:
        #     turn nums into set to inorder to reduce the memory, 
        #     check ele-1 in nums also in numset, if yes, it is the start of a new sequence
        #     keep track of the longest strike while incrementing ele by 1 if it is the longest update the global longest
        
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            if n-1 not in numSet:
                length = 1
                while(n+length) in numSet:
                    length += 1
                longest = max(longest,length)
        return longest
print(Solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))