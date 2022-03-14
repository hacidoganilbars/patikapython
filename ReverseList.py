
myList = []

def reverseList(l):
    for i in l:
        if type(i)==list:
            i.reverse()
        myList.append(i)
    myList.reverse()
    return myList

result = reverseList([[1, 2], [3, 4], [5, 6, 7]])
print(result)