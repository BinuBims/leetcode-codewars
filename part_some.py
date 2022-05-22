def parts_sums(ls):
#         pseudo code:
#         get the sum of all the elements in an array part_sum = [sum(ls)]
#         for loop(len of ls) to append updated value part_sum[i]-ls[i]
#         return that part_sum
    
    part_sum = [sum(ls)]
    
    for i in range(len(ls)):
        part_sum.append(part_sum[i]-ls[i])
    return part_sum
        

print(parts_sums([1,3,5,6]))