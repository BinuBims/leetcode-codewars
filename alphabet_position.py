# Welcome.

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

def alphabet_position(text):
    result_array = []
    for char in text.lower():
      if char.isalpha():
        result_array.append(str(ord(char)-96))
    return " ".join(result_array)