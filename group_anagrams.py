from collections import defaultdict
class Solution:

    def groupAnagrams(strs):
        #input: an array of string
        #output: nested string arrays of an array
        res = defaultdict(list)
        for s in strs:
            count = [0]*26 #A to Z
            for c in s:
                count[ord(c)-ord('a')] += 1 # ascii(char)-ascii("a") ex: b-a = 1, 81-80 = 1
            res[tuple(count)].append(s) #had to turn into tuple inorder to put in the dictionaty also make sure to append the substring from the input string
        return res.values()
        
  
        #ex:strs = ["eat","tea","tan","ate","nat","bat"] =>Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))   