def count_down_from(number):
    if number != 0:
        print(number)
        count_down_from(number-1)


count_down_from(5)