num=int(input("enter the number: "))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(2,num):
    res=a+b
    print(res,end=" ")
    a=b
    b=res

