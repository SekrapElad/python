count = 0

while count < 5:
    print(f"Number: {count}")
    count += 1


def fizzbuzz(number):
    loop_count = 1
    while loop_count <= number:
        if loop_count % 3 == 0 and loop_count % 5 != 0:
            print("Fizz")
        elif loop_count % 5 == 0 and loop_count % 3 != 0:
            print("Buzz")
        elif loop_count % 5 == 0 and loop_count % 3 == 0:
            print("Fizzbuzz")
        else:
            print(loop_count)

        loop_count += 1


fizzbuzz(30)