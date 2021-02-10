# values = [3, 6, 9, 12, 15, 18]
# other_vals = [5, 10, 55, 20, 25, 30]

# def odds_sum(vals):
#     sum = 0
#     for val in vals:
#         if val % 2 != 0:
#             sum += val

#     return sum

# print(odds_sum(other_vals))

# def greatest_number(numbers):
#     greatest_num = numbers[0]

#     for number in numbers:
#         if number >= greatest_num:
#             greatest_num = number
    
#     return greatest_num

# print(greatest_number(other_vals))

def super_sum(list_strings):
    s_sum = 0
    
    for string in list_strings:
        if 's' in string:
            s_sum += string.index('s')
    return s_sum

print(super_sum(["mustache", "pessimist"]))