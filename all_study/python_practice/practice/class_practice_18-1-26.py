class gift:
    def __init__(self,code,price,gift_type):
        self.code=code
        self.price=price
        self.type=gift_type

    def __str__(self):
        return f'code: {self.code} price: {self.price}, type: {self.type}'

    def isForMan(self):
        if self.type == 'M' or 'U':
            return True
        return False



def giftForMan(gifts,sumi):

    flag=False
    for i in range(len(gifts)):
        g1=gifts[i]
        if g1.isForMan() and g1.price < sumi:
            for j in range(i,len(gifts)):
                g2=gifts[j]
                if g2.isForMan() and g1.price+g2.price <sumi:
                    for h in range(j,len(gifts)):
                        g3=gifts[h]
                        if g3.price+g2.price+g1.price==sumi:
                            flag=True
                            print(f'{g1} , {g2} , {g3}')
    if flag==False:
        print("nothing!")
                        






def ex11a(c,b):
    a=[]
    for item in c:
        if item in b and item not in a:
            a.append(item)
    return a


def ex11a(c,b):
    a=[]
    for item in c:
        flag=True
        for item2 in b:
            if item2==item:
                flag=False
        if flag:
            a.append(item)
    return a


def cleanWeight(num):
    sum=0
    while num>=10:
        sum+=num%10
        num//10
    return sum

def isCleanWeightArr(arr):
    for i in range(len(arr)-1):
        if cleanWeight(arr[i])>cleanWeight(arr[i+1]):
            return False
    return True

def uniqeCleanWeight(arr1,arr2):
    i,j=0,0
    new_arr=[]

    while i<len(arr1) and j < len(arr2):
        cw1=cleanWeight(arr1[i])
        cw2=cleanWeight(arr2[j])
        if cw1 < cw2:
            new_arr.append(arr1[i])
            i+=1
        elif cw1==cw2:
            i+=1
            j+=1
        elif cw1 > cw2:
            new_arr.append(arr2[j])
            j+=1

    if i <len(arr1):
        for index in range(i,len(arr1)):
            new_arr.append(arr1[index])

    if j < len(arr2):
        for index in range(j,len(arr2)):
            new_arr.append(arr2[index])
    return new_arr



def uniqueCleanWeight2(arr1, arr2):
    i, j = 0, 0
    new_arr = []

    while i < len(arr1) and j < len(arr2):
        cw1 = cleanWeight(arr1[i])
        cw2 = cleanWeight(arr2[j])

        if cw1 < cw2:
            new_arr.append(arr1[i])
            i += 1
        elif cw1 == cw2:
            # התיקון: מוסיפים אחד מהם לרשימה לפני שמקדמים את שניהם
            new_arr.append(arr1[i]) 
            i += 1
            j += 1
        elif cw1 > cw2:
            new_arr.append(arr2[j])
            j += 1

    # הוספת השאריות (זה היה מצוין בקוד שלך)
    if i < len(arr1):
        for index in range(i, len(arr1)):
            new_arr.append(arr1[index])
            
    if j < len(arr2):
        for index in range(j, len(arr2)):
            new_arr.append(arr2[index])
    print(new_arr)
    return new_arr

arr1= [35,923,781,12349,1892]
arr2 = [2,358,181,5821,1742,36621,27731]


print(uniqueCleanWeight2(arr1,arr2))







