class Solution:
    def twoSum(numbers, target):
        # pseudo code:
        #     l and r pointer, l start at the begining and right start at the end
        #     since the array is sorted check if the sum of numbers[l]+numbers[r]>target then r -=1
        #     if the sum of numbers[l]+numbers[r]<target then r +=1
        #     if the sum of numbers[l]+numbers[r]=target then return index

        
        l,r = 0, len(numbers)-1
        
        while l<r:
            if numbers[l]+numbers[r]>target:
                r -=1
            if numbers[l]+numbers[r]<target:
                l +=1
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]

print(Solution.twoSum([2,7,11,15],9))