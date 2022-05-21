class Solution:
    def plusOne(digits):
        # pseudo code: combine the array and turn that into an integer
        #              Then, add one to that number 
        #              return a list that seperate those number into a single num
                
        num = ''
        digits = [str(n) for n in digits]
        for n in digits:
            num += n
        num_ = int(num)+1
        return [int(i) for i in str(num_)]

print(Solution.plusOne([3,2,4]))