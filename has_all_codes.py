class Solution:
    def hasAllCodes(s,k):
        check_set = set()
        for i in range(len(s)-k+1):
            check_set.add(s[i:i+k])
        return len(check_set)==2**k

s = "00110110"
k = 2
print(Solution.hasAllCodes(s,k))
