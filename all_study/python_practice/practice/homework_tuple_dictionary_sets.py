
#tuple
def ex1(t):
    biggest=t[0]
    smallest=t[0]
    sum=0
    for tempeture in t:
        sum+=tempeture
        if tempeture>biggest:
            biggest=tempeture
        if tempeture<smallest:
            smallest=tempeture
    return (biggest,smallest,sum/len(t))
        
def ex2(t):
    new_list=[]
    for point in t:
        length=(point[0]**2+point[1]**2)**0.5
        new_list.append(length)
    return tuple(new_list)

def ex3(t):
    for x in range(1,len(t)-1):
        if t[x-1]<t[x]<t[x+1]:
            return True
    return False

def ex4(t):
    x=0
    y=0
    for step in t:
        match step:
            case "R":
                x+=1
            case "L":
                x-=1
            case "U":
                y+=1
            case "D":
                y-=1
    return (x,y)

#sets
def ex5(set1,set2):
    return len(set1|set2)

def ex6(set1,set2):
    return set1 & set2

def ex7(set1,set2):
    return set1 - set2

def ex8(set1,set2):
    return set2 - set1

#dict
def ex9(dict):
    sum=0
    for name in dict:
        sum+=dict[name]
    return sum/len(dict)

def ex10(l):
    new_dict={}
    for word in l:
        if word not in new_dict.keys():
            new_dict[word]=l.count(word)
    return new_dict

def ex11(dict):
    under_18=[]
    for name in dict:
        if dict[name] < 18:
            under_18.append(name)
    return under_18

def ex12(dict,l):
    for item in l:
        dict[item]-=1
    return dict

def ex13(dict):
    jobs={}
    for name in dict:
        job=dict[name]
        if job not in jobs.keys():
            jobs[job]=[name]
        else:
            for i,name2 in enumerate(jobs[job]):
                if name < name2:
                    jobs[job].insert(i,name)
                    break
                if i==len(jobs[job])-1:
                    jobs[job].append(name)
                    break
    return jobs

def ex14(dict):
    new_dict={}
    for key in dict:
        # key != {} and key != [] keys cannot be dictionary or list
        if key is not None:
            new_dict[key]=dict[key]
    return new_dict

