"""A1 - 037"""
def roman(num):
    """roman"""
    hun = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    ten = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    one = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    th , left = divmod(num,1000)
    hu , left = divmod(left,100)
    te , on = divmod(left,10)
    m = th * "M"
    return f"{m}{hun[hu]}{ten[te]}{one[on]}"

print(roman(int(input())))
