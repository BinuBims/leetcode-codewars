def century(year):
    if year <= 100:
        return 1
    elif year % 100 == 0:
        return int(str(year)[:-2])
    else:
        return int(str(year)[:-2])+1
    # Finish this :)
#     input >> year(int)
#     output >> what century(int)
#     test_cases:
#         1705 --> 18
#         1900 --> 19
#         1601 --> 17
#         2000 --> 20
#     if less than  100;
#     should be 1
#     else divide year by 100
#     if no remainder
#     return [:-2]
#     if remainder
#     return [:-2]+1

print(century(1705))