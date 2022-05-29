class Solution:
    def maxProduct( words) -> int:
        char_set = [set(words[i]) for i in range(len(words))]
        max_len = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not (char_set[i] & char_set[j]):
                    max_len = max(max_len, len(words[i]*len(words[j])))
        return max_len

print(Solution.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))