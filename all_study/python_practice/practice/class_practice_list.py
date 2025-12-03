def class_grades(numOfStudents):
    l=[]
    for i in range(numOfStudents):
        grade=int(input(f"enter student {i+1} grade: "))
        l.append(grade)
    a=sum(l)/len(l)
    amount_under=0
    for g in l:
        if g<a:
            print(f"{g} is under the avarage")
            amount_under+=1
        else: print(f"{g} is above avg")
    print(f'there are {amount_under} of students under the avg')

def rain_min_max():
    months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]
    min_rain=int(input('enter how much rain in month 1: '))
    max_rain=min_rain
    l=[min_rain]
    for i in range(2,13):
        rain=int(input(f'enter how much rain in month {i}: '))
        l.append(rain)
        if rain<min_rain:
            min_rain=rain
        if rain>max_rain:
            max_rain=rain
    for i,rain in enumerate(l):
        if rain==min_rain:
            print(f'min rain in {months[i]}')
        if rain==max_rain:
            print(f'max rain in {months[i]}')
def amount_of_numbers(num):
    l=[0]*10
    while num>0:
        digit=num%10
        l[digit]+=1
        num//=10
    for i,sum in enumerate(l):
        if sum>0:
            print(f'number {i} can be found {sum} times')
            
def ex1a(n):
    l=[]
    l.append(int(input('enter number 1: ')))
    min=l[0]
    sum=0
    count=0
    for i in range(1,n):
        num=int(input(f'enter number {i+1}: '))
        l.append(num)
        if num<min:
            sum+=num
            count+=1
    print(sum/count)

def ex1b(n):
    l=[]
    for i in range(0,n):
        num=int(input(f'enter number {i+1}: '))
        l.append(num)
    sum=0
    count=0
    last=l[len(l)-1]
    for i,val in enumerate(l):
        if(val<last):
            sum+=val
            count+=1
    print(sum/count)

def ex3(a,n):
    for x in range(1,n+1):
        if(x not in a):
            print(x)
            return x

