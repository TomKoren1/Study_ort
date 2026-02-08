def ex1a(s): #test ci2
    count=0
    for i,c in enumerate(s):
        if c=='a':
            for j in range(i,len(s)):
                if s[j]=='b':
                    count+=1
    print(f'number of sequences whre it start with a and end with b: {count}')
def ex1b(s):
    count=0
    for i,c in enumerate(s):
        if c=='a':
            for j in range(i,len(s)):
                if s[j]=='b':
                    count+=1
                if s[j]=='c':
                    break
    print(f'number of sequences whre it start with a and end with b and dosent contain c between: {count}')  
def ex1c(s):
    count=0
    for i,c in enumerate(s):
        if c=='a':
            c_count=0
            for j in range(i,len(s)):
                if s[j]=='b' and c_count==1:
                    count+=1
                if s[j]=='c':
                    c_count+=1
                if c_count>1:
                    break
    print(f'number of sequences whre it start with a and end with b with one c between: {count}')     
def ex1():
    inp=''
    while(inp!='.'):
        s+=inp
        inp=input('enter a character from abc: ')
    ex1a(s)
    ex1b(s)
    ex1c(s)

def ex2():
    all_str='all the strings that start and end in the same character:'
    for i in range(15):
        s=input(f'enter string number {i}: ')
        if s[0]==s[len(s)-1]:
            all_str+=f' {s},'
    print(all_str[:len(all_str)-1])

def ex3(s1,s2):
    min_str=s1
    max_str=s2
    if len(s1)>len(s2):
        max_str=s1
        min_str=s2
    if len(max_str)>len(min_str)*2:
        print(max_str)
    else:
        print(min_str)

def ex4(s1,s2):
    count=0
    for i,c in enumerate(s1):
        if c== s2[0]:
            for j in range(len(s2)):
                if s1[i+j]!=s2[j]:
                    break
                if j==len(s2)-1:
                    count+=1
    print(count)

def ex5(s):
    sum=0
    num=0
    for c in s:
        if c>='0' and c<='9':
            num=num*10+int(c)
        else:
            sum+=num
            num=0
    print(sum)
def ex6(s,seperator):
    new_s=''
    for c in s:
        if c != seperator:
            new_s+=c
    print(new_s)

def ex7(s,key):
    new_s=''
    for i,c in enumerate(s):
        if(ord(c)+key<=ord('Z')):
            new_s+=chr(ord(c)+key)
        else:
            new_s+=chr(ord('A')+key-ord('Z')+ord(c)-1)
    print(new_s)
ex7('BABY',3)
