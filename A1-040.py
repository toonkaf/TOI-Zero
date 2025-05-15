"""A1 - 040"""
def cal():
    """calories"""
    kept = 0
    dic = {1 : 100 , 2 : 120 , 3 : 200 , 4 : 60}
    while True:
        x = int(input())
        if x == 5:
            break
        kept += dic[x]
    print(f"Bye Bye\nTotal Calories: {kept}")

cal()
