
def some():
    return False,12

a,b=some()
print(a,b)





def all1(arr):
    flag=True
    for num in arr:
        flag=(num==1 and True)
        print(flag)
    return flag

arr=[1,1,1,1,1,1]

all1(arr)