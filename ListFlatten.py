
myList = []

def flatten(l):
    for i in l:
        if type(i)==list:
            flatten(i)
        else:
            myList.append(i)
    return myList

result = flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(result)