



a=[0,1,2]
b=[3,4,5]
c=[6,7,8]

matrix=[a,b,c]


print(matrix)

def func1(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if j==1:
                print(mat[i][j])
    return 1

def findMax(a,b,numbers):
    if a>b:
        return a
    if a<b:
        return b

def count_example(numbers):
    counter=0
    for num in numbers:
        if num == 1:
            counter+=1
    return counter

def find_max(numbers):
    max_number=numbers[0]
    for num in numbers:
        if num > max_number:
            max_number=num
    return max_number


def something():
    return 1,2

a,b=something()
print(f"a: {a} , b:{b}")