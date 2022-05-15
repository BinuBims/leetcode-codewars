#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
class Solution:
    def topKFrequent(nums, k):
        #input: an array of numbers
        #output: output a list with most repeated numbers, do it for time k number of time.
        #ex: nums = [1,1,1,2,2,3], k = 2 >> [1,2]
        #psuedo code:
            #for loop to keep track how many times a number is repeated and that to a dictionary
            #while loop to get the key of the max value and append it to a list, then delete that max key from the dictionay, repat that k times.
        count_dict = {}
        output_list = []
        for i in nums:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        while k>0:
            max_val = max(count_dict,key=count_dict.get)
            output_list.append(max_val)
            del count_dict[max_val]
            # print(output_list)
          
            k -=1
        return output_list

print(Solution.topKFrequent([1,1,1,2,2,3,3,3], 2))