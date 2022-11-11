# There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

# A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

# As a simplification, you may assume that no letter occurs more than once in the secret string.

# You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.

# output should equal secret = "whatisup"
def recoverSecret(triplets):
  all_char = list(set([i for triplet in triplets for i in triplet]))
  for triplet in triplets:
    arrange(all_char,triplet[1],triplet[2])
    arrange(all_char,triplet[0],triplet[1])
  return "".join(all_char)
def arrange(all_char,a,b):
  if all_char.index(a)>all_char.index(b):
    all_char.remove(a)
    all_char.insert(all_char.index(b),a)


triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))