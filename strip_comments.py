# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas
def strip_comments(strng, markers):
    words = strng.split('\n')
    for marker in markers:
        words = [word.split(marker)[0].rstrip() for word in words]
    return "\n".join(words)

print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))