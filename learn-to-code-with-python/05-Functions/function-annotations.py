# Params are done using "var: <type>" pattern.
# Return value done using "-> <type>".
def word_multiplier(word: str, times: int) -> str:
    return word * times

print(word_multiplier("dog", 5))