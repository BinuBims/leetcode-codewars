# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
class Solution:
    def isIsomorphic(s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i, j in zip(s,t):
          s_dict[i] = j
          t_dict[j] = i
        print(s_dict, t_dict)
        return list(s_dict.keys()) == list(t_dict.values())

print(Solution.isIsomorphic('egg','add'))
print(Solution.isIsomorphic('foo','bar'))