def count_num_len(n):
    if n>0:
        return 1+count_num_len(n//10)
    else:
        return 0
def sum_of_digits(n):
    if n>0:
        return n%10+sum_of_digits(n//10)
    else:
        return 0
    
def fibo_rek(n1,n2,end):
    print(f"{n1},",end="")
    if n1+n2 <end:
        fibo_rek(n2,n1+n2,end)
    else:
        print(n2)

def fibo(end):
    n1=1
    n2=1
    while(n1+n2<end):
        print(f"{n1}, ",end="")
        temp=n2
        n2=n2+n1
        n1=temp
    print(f"{n1}, {n2}")
    return n2

def sum_of_array(arr):
    if len(arr)>0:
        new_list=arr
        return new_list.pop() + sum_of_array(new_list)
    return 0
def sum_of_array_2(arr):
    if len(arr)>0:
        return arr[0]+sum_of_array_2(arr[1:])
    else:
        return 0

def merge_3_array(a,b,c):
    i1=0
    i2=0
    while i1<len(a) and i2<len(b):
        if a[i1]<=b[i2]:
            c.append(a[i1])
            i1+=1
        else:
            c.append(b[i2])
            i2+=1
    while i1<len(a):
        c.append(a[i1])
        i1+=1
    while i2<len(b):
        c.append(b[i2])
        i2+=1
    
    print(c)

merge_3_array([1,2,4,10],[1,8,9],[])

