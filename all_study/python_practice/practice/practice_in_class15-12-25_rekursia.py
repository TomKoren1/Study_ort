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

fibo(300)