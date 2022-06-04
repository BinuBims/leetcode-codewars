# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

def expanded_form(num):
#     while loop to continue till num is less than 10:
#         get the length of num and first num, reduce it from the number
#         add it to the empty string

    final_string = []
    num_list = list(str(num))
    print(num_list)
    while num>0:
        reduce_num = str(num_list[0])+str(0)*(len(num_list)-1)
        num_list.pop(0)
        
        final_string.append(reduce_num)
        num -= int(reduce_num)
    before_join = [num if int(num)!=0 else '' for num in final_string]
    return (" + ").join((" ").join(before_join).split())
