# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        left_point = 0
        right_point = 0
        while left_point < len(s) and right_point < len(t):
            if s[left_point] == t[right_point]:
                left_point += 1
            right_point += 1
        return len(s) == left_point
