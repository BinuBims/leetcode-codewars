class Solution:
    def runningSum(nums):
        # for loop to iterate over nums list:
        #     add each num to runing sum
        #     append that final sum after each iteration to result list
        result = []
        runing_sum = 0
        for num in nums:
            runing_sum += num
            result.append(runing_sum)
        return result
print(Solution.runningSum([1,2,3,4]))