# browsers = ['Chrome', 'Firefox', 'Safari', 'Opera']

# print(browsers[0])
# print(browsers[2])
# print(browsers[2][1])
# print(browsers[-1])

def product_of_even_indices(list_numbers):
    product = 1
    index = 0
    
    while index <= len(list_numbers) - 1:
        if index % 2 == 1:
            product *= list_numbers[index]
        
        index += 1
        
    return product

print(product_of_even_indices([1, 2, 3, 4, 5, 6]))