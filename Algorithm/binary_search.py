def binary_search(list:list,val):
    left,right=0,len(list)-1
    while left<=right: #候选区有值
        mid=(left + right)//2
        if list[mid]==val:
            return mid
        elif list[mid]>val: #查找的值在mid的左侧，right=mid-1
            right=mid-1
        elif list[mid]<val: #查找的值在mid右侧,left=mid+1
            left=mid+1
    else:
        return None
print(binary_search([1,2,3],2))