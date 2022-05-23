class Solution:
    def lengthOfLastWord(s) :
#         pseudo code:
#             use slice to hold on to last word
#             get the length of last word
        return len(s.split()[-1])

print(Solution.lengthOfLastWord("   fly me   to   the moon  "))