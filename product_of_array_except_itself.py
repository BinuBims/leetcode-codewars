class Solution:
    def productExceptSelf(nums):
        # input: an array of numbers
        # output: an array of numbers where answer[i] is equal to product of all the elements except nums[i]
        # Pseudo code:
        #  empty array to the size of num call this result
        #  for loop to mutiply every numbers before the current number and store the product in the same position as the current number in result
        #  for loop to multiply every numbers after the current number but in this case, start from the end of the array
        #  multipy the products of the second for loop by result array to update the values in the array.

                
        res = [0]*len(nums)
        pre = 1
        for i in range(0,len(nums)):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post *= nums[i]
            
        return res

print(Solution.productExceptSelf([1,2,3,4]))