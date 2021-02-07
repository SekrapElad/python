# name, adjective, noun
# mad_libs = "{} laughed at the {} {}."

# print(mad_libs.format("Dale", "green", "dog"))

# Can also use indexes.
# mad_libs = "{0} laughed at the {1} {2}."
# print(mad_libs.format("Dale", "green", "dog"))

# mad_libs = "{2} laughed at the {0} {1}."
# print(mad_libs.format("Dale", "green", "dog"))

# mad_libs = "{0} laughed at the {2} {0}."
# print(mad_libs.format("Dale", "green", "dog"))

# Can use words instead of indexes.
mad_libs = "{name} laughed at the {adjective} {noun}."

print(mad_libs.format(name = "Dale", adjective = "green", noun = "dog"))
# name = input("Enter a name: ")
# adjective = input("Enter an adjective: ")
# noun = input("Enter a noun: ")

# print(mad_libs.format(name = name, adjective = adjective, noun = noun))

