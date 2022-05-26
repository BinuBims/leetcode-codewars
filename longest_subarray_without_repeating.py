class Solution:
    def lengthOfLongestSubstring(s):
        l = 0
        isDuplicate = set()
        res = 0
        for r in range(len(s)):
            while s[r] in isDuplicate:
                isDuplicate.remove(s[l])
                l += 1
            isDuplicate.add(s[r])
            res = max(res,r-l+1)
        return res
print(Solution.lengthOfLongestSubstring("abcabcbb"))