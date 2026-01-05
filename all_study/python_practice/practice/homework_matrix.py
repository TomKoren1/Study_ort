

def ex1(mat):
    for i in range(len(mat)//2):
        if mat[i][i]!=mat[len(mat)-i-1][len(mat)-i-1]:
            return False
    return True

def ex2(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]!=mat[j][i]*-1:
                return False
    return True

def ex3(mat):
    for i in range(len(mat)):
        for j in range(1+i,len(mat)):
            if mat[i][j]!=0:
                return False
    return True

def ex4(mat):
    for i in range(1,len(mat)):
        for j in range(0,i-1):
            if mat[i][j] != 0:
                return False
    return True

def ex5(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i!=j and mat[i][j]==0:
                return False
    return True

def ex6(mat):
    temp=mat[0][0]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j and mat[i][j]!=temp:
                return False
            if i!=j and mat[i][j]!=0:
                return False
    return True

def ex7(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]!=0:
                return False
    return True

def ex8(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j and mat[i][j]!=1:
                return False
            if i!=j and mat[i][j]!=0:
                return False
    return True

def ex9(mat):
    count=0
    for i in range(1,len(mat)-1):
        for j in range(1,len(mat[0])-1):
            if mat[i][j]==0 and mat[i-1][j]==1 and mat[i][j-1]==1 and mat[i-1][j-1]==1:
                count+=1
    return count

def ex10(mat):
    new_mat=[]
    for i in range(len(mat)):
        new_row=[]
        for j in range(len(mat[0])):
            value=0
            for n in range(-1,2):
                for n2 in range(-1,2):
                    if len(mat)>i+n>=0:
                        if len(mat)>j+n2>=0 and not (n2==0 and n==0):
                            print(f"i:{i}, j:{j}, n:{n}, n2:{n2}")
                            value+=mat[i+n][j+n2]

            new_row.append(value)
        new_mat.append(new_row)
    return new_mat
                        



matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
need_to_return=[
[11, 20, 13],
[24, 40, 24],
[17, 28, 17]
]


data=(1,2,3)
t=list(data)
print(t)