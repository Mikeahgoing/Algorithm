def liner_search(list:list,val):
    for index,v in enumerate(list):
        if v==val:
            return index
    else:
        return None
        
print(liner_search([1,2,3],2))