# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]

def array_diff(a, b):
    for i in b:
      while i in a:
        a.remove(i)
    return a

print(array_diff([1,2,3], [1, 2]))