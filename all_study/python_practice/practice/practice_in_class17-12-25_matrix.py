
def print_matrix(matrix):
    print(f" [")
    for arr in matrix:
        print(f"    {arr}")
    print(" ]")
def is_ribui(arr):
    n=len(arr)
    for i,item in enumerate(arr):
        if len(item) != n:
            return False
    return True

def matrix_sum(matrix):
    sum=0
    for arr in matrix:
        sum+=sum(arr)
    return sum

def get_j(matrix,j):
    for arr in matrix:
        print(f"{arr[j]}  ",end="")

def no_ends_matrix(matrix):
    for arr in matrix:
        arr.pop()
        arr.pop(0)
    return matrix[1:-1]

def new_matrix(arr1,arr2):
    matrix=[]
    for i in arr1:
        new_arr=[]
        for j in arr2:
            new_arr.append(i*j)
        matrix.append(new_arr)
    return matrix

def sort_matrix_by_sum(matrix):
    for i,arr1 in enumerate(matrix):
        sum1=sum(matrix[i])
        print(f"{i}: ")
        print_matrix(matrix)
        for j,arr2 in enumerate(matrix):
            sum2=sum(matrix[j])
            if sum1<sum2:
                temp=matrix[i]
                matrix[i]=matrix[j]
                matrix[j]=temp
                sum1=sum(matrix[i])
                sum2=sum(matrix[j])
    return matrix


def sort_matrix_by_sum2(matrix):
    sums=[]
    for i in range(len(matrix[0])):
        sum=0
        for j in range(len(matrix)):
            sum+=matrix[j][i]
        sums.append(sum)
    print(f" sums: {sums}")

    for i in range(len(sums)):
        for j in range(len(sums)):
            if sums[i]<sums[j]:
                temp=sums[i]
                sums[i]=sums[j]
                sums[j]=temp
                for arr in matrix:
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp



def paint_mat(mat,i,j,n):
    temp=mat[i][j]
    mat[i][j]=n
    for num1 in range(-1,2):
        for num2 in range(-1,2):
            if 0<=i+num1< len(mat) and 0<=j+num2<len(mat[i+num1]):
                if mat[i+num1][j+num2]==temp:
                    paint_mat(mat,i+num1,j+num2,n)


mat=[
    [3,3,3],
    [3,2,3],
    [1,2,3]
]
paint_mat(mat,1,2,5)
print_matrix(mat)
