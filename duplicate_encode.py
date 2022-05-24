def duplicate_encode(word):
#     pseudo code:
#         a dictionary figure if it a char is a duplicate or not
#         an array of "(" that equal length of input(word)
#         an empty list
#         for loop the word if char not in the empty list add that to empty list, if it is already in change "(" to ")"
#         return the the final array
    word = word.lower()
    count_dict = {}
    result = ["("]*len(word)
    for v in word:
        if v not in count_dict:
            count_dict[v] = 1
        else:
            count_dict[v] +=1
    for i,v in enumerate(word):
        if count_dict[v]>1:
            result[i] = ")"
    return ('').join(result)

print(duplicate_encode("hello world"))