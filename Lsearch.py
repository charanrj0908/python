pos = 0
def search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    else:
        return False



list=[2,5,6,8,9]
n=int(input("enter value to search : "))
if search(list,n):
    print("found at index -",pos)
else:
    print("not found")