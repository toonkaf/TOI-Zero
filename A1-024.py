"""A1 - 024"""
def tax(year,cc):
    """tax"""
    lst = [[1250,1400,2000],[1100,1300,1700],[1000,1200,1500]]
    year = min(max(-1,year-1991) // 10 , 1) + 1
    cc = min(max(-1,cc-1501) // 500 , 1) + 1
    return lst[year][cc]

print(tax(int(input()),int(input())))
