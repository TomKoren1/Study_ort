import random

def show_list_max(l):
    max_index=0
    max_item=l[0]
    for i,item in enumerate(l):
        if item>max_item:
            max_item=item
            max_index=i
    temp=l[-1]
    l[-1]=max_item
    l[max_index]=temp
    return l

def bubble_sort(L):
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if L[i]>L[j]:
                temp=L[i]
                L[i]=L[j]
                L[j]=temp
def selection_sort(L):   
    for i in range(len(L)-1,0,-1):
        max_item=L[i]
        max_index=i
        for j in range(0,i):
            if max_item<L[j]:
                max_index=j
                max_item=L[j]
        temp=L[i]
        L[i]=max_item
        L[max_index]=temp
def insertion_sort(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            flag=False
            for j in range(0,i):
                if arr[j]> arr[i] or flag==True:
                    temp=arr[j]
                    arr[j]=arr[i]
                    arr[i]=temp
                    flag=True
                    
                

        

def index_from_sorted(l,n):
    start=0
    end=len(l)-1
    middle=(start+end)//2
    while(end!=start):
        middle=(start+end)//2
        if l[middle]==n:
            return middle
        if l[middle]>n:
            end=middle
        if l[middle]<n:
            start=middle
    return middle

def merge_sorted_lists_to_else(sorted_list1,sorted_list2,l):
    new_list=[]
    index1=0
    index2=0
    for item in l:
        if item < sorted_list1[index1] and item < sorted_list2[index2]:
            new_list.append(item)
        else:
            if sorted_list1[index1]> sorted_list2[index2]:
                print()

                
l=[10,23,31,45,3,2,8,9]
insertion_sort(l)
print(l)


