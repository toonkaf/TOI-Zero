"""A1 - 007"""
def checker(str):
    if str in ('a','e','i','o','u'):
        return "yes"
    return "no"

print(checker(input()))
