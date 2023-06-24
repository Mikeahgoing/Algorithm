#这个方法的时间复杂度非常高，不建议使用
def select_sort_simple(list:list)->list:
    new_list=[]
    for i in range(len(list)):
        min_val=min(list)
        new_list.append(min_val)
        list.remove(min_val)
    return new_list
print(select_sort_simple([3,2,1,4]))

def select_sort(list:list)->list:
    for i in range(len(list)-1):
        min_loc=i
        for j in range(i+1,len(list)):
            if list[j]<list[min_loc]:
                min_loc=j
        list[i],list[min_loc]=list[min_loc],list[i]
        return list
print(select_sort([3,2,1]))