"""A1 - 012"""
def swap(num: int,oprt : str):
    """+ * ="""
    num2 = int(str(num)[::-1])
    if oprt == "+":
        return f"{num} + {num2} = {num+num2}"
    return f"{num} * {num2} = {num * num2}"

print(swap(int(input()),input()))
