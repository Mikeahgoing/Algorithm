def bubble_sort(list:list)->list:
    for i in range (len(list)-1):
        exchange=False #用标志位对冒泡排序进行优化,当前面已经排好了就不用继续执行了
        for j in range (len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                exchange=True
        if not exchange:
            return
list=[2,1,3,4]
bubble_sort(list)
print(list)