def last_in_list_switch(arr,b):
    if not b:
        last=arr[-1]
        arr.insert(0,last)
        arr.pop()
    else:
        new_list=[arr[-1]]
        for i in range(len(arr)-2):
            new_list.append(arr[i])
        return new_list

def sort_3_items_list(arr):
    biggest_index=0
    smallest_index=0
    
    new_list=[]
    for i,item in enumerate(arr):
        if arr[i]>arr[biggest_index]:
            biggest_index=i
        if arr[i]<arr[smallest_index]:
            smallest_index=i
    new_list.append(arr[smallest_index])
    for item in arr:
        if item > arr[smallest_index] and item < arr[biggest_index]:
            new_list.append(item)
    new_list.append(arr[biggest_index])
    return new_list

def merge_sorted_lists(arr1,arr2):
    index1=0
    index2=0
    new_list=[]
    for i in range(len(arr1)+len(arr2)):
        if index1 <=len(arr1)-1 and arr1[index1]<arr2[index2]:
            new_list.append(arr1[index1])
            index1+=1
        else:
            new_list.append(arr2[index2])
            index2+=1
    return new_list
    
    
def get_clean_weight(num):
    num//=10
    full_weight=0
    while num>10:
        full_weight+=num%10
        num//=10
    return full_weight

def check_sorted_by_weight(list):
    for i in range(len(list)-1):
        if get_clean_weight(list[i])>get_clean_weight(list[i+1]):
            return False
    return True

