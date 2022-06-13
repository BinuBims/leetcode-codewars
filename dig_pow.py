def dig_pow(n, p):
    #pseudo code:
    # do a for loop get the total, check if the total divided by n without remainder, if not return -1
    n_list = [int(n) for n in list(str(n))]
    total = 0
    for num in n_list:
      total += num**p
      p += 1
    return total // n if total % n == 0 else -1