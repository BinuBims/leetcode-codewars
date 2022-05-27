class Solution:
    def numberOfSteps(num: int) -> int:
        # pseudo code:
        #     while loop till num<0
        #         if the current num is odd, reduce one
        #         divide by 2 and keep track
        #         update num with divided num
        
        count = 0
        while num>0:
            if num%2 ==1:
                num = num-1
                count+=1
            elif num!=0:
                num = num/2
                count += 1
        return count

print(Solution.numberOfSteps(123))