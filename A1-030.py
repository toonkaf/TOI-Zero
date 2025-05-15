"""A1 - 030"""
def sumn(n , m : list):
    """sumn"""
    lst = []
    kept = ""
    for i in range(n):
        lst.append(max(int(m[0]),int(m[1])))
        if not i :
            kept += f"{lst[i]} "
        else:
            kept += f"+ {lst[i]} "
        m.pop(0)
        m.pop(0)
    if n > 1:
        kept += "= "
    else:
        kept = ""
    return f"{kept}{sum(lst)}"

print(sumn(int(input()),input().split()))
