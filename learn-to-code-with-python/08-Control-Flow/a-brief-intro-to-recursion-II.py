# def reverse(str):
#     length = len(str)
#     reversed_str = ""
#     while length > 0:
#         reversed_str += str[length-1]
#         length -= 1
    
#     return reversed_str 

def reverse(str):
    if len(str) <= 1:
        return str

    return str[-1] + reverse(str[:-1])
    

print(reverse('Dale Parkes'))