"""A1 - 031"""
def luknam(num):
    ""","""
    return num[:-3] + "," + num[-3:]

print(luknam(input()))
