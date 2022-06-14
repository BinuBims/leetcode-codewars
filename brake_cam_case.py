# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
def solution(s):
    result = []
    for i in range(len(s)):
        if s[i] == s[i].upper():
            result.append(' '+s[i])
        else:
            result.append(s[i])
    return ''.join(result)