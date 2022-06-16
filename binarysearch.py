pos = -1

def search(list,n):
    LB = 0
    UB = len(list) - 1
    while LB <= UB:
        MB = (LB + UB) // 2
        if list[MB] == n:
            globals()['pos'] = MB
            return True
        else:
            if list[MB] < n:
                LB = MB + 1
            else:
                UB = MB - 1
    return False




list=[4,7,8,12,45,99]
n=int(input("enter value to search : "))
if search(list,n):
    print("found at index :",pos)
else:
    print("not found")