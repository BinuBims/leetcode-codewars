# You are given an array(list) strarr of strings and an integer k. Your task is to return the 
# first longest string consisting of k consecutive strings taken in the array.

# ex: ["zone", "abigail", "theta", "form", "libe", "zas"], 2) should equal "abigailtheta"

def longest_consec(strarr, k):
    # if k<o also return empty array
    # for loop to join kth number of word
    # append it to new list
    # get the max of the list(key=len)
    count_starr = []
    if k<0:
        return ""
    for i in range(0,len(strarr)-k+1):
        count_starr.append("".join(strarr[i:i+k]))
    return max(count_starr, key=len) if count_starr else ""

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))