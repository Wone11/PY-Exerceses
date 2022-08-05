'''
Add Item and its index and append to new list
'''
def add_indexes(lst):
    newlst=[]
    for index,item in enumerate(lst):
        newlst.append(item + index)
        
    return newlst