def ex1():
    for i in range(1,1001):
        temp=i
        flag=True
        while temp>0:
            if temp%10 == 0:
                flag=False
            if flag and i % (temp%10)!=0:
                flag=False
            temp//=10
        if flag:
            print(i)


