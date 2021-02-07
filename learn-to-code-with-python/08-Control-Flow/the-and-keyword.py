def check_number(number):
    if number < 10:
        print("Less than 10")
    elif number >= 10 and number < 25:
        print("More than or equal to 10, but less than 25")
    else:
        print("More than 25!")


check_number(12)