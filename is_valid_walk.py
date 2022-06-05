def is_valid_walk(walk):
    # a dict to keep track of letter
    # if len(walk) == 10 -> do a for loop to add letter count to dictionary
    # if number of n and s and number of w and e equal return true
    
    count_dict = {'n':0,'s':0,'w':0,'e':0}
    if len(walk)==10:
        for block in walk:
            count_dict[block] +=1
        if count_dict['n'] == count_dict['s'] and count_dict['w'] == count_dict['e']:
            return True
    return False