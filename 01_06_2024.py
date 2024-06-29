#Задание 2
list1=(4,5,5,1,2,3,4,8,1)
def slicer(x,el):
    score=0
    for i in range(len(x)):
        if el == x[i]:
            score+=1
    if score>=2:
        newlist = list(x)
        newlist.insert(0, el)
        newlist.append(el)
        newlist = tuple(newlist)
        return newlist
    elif score==1:
        newlist = list(x)
        newlist.insert(0, el)
        return newlist
    else:
        newlist=tuple()
        return tuple
print(slicer(list1,2))

#Задание 3
list1=[4,5,5,1,2,3,4,8,1]
def sieve(x):
    newx=tuple(sorted(set(x),reverse=True))
    return newx
print(sieve(list1))


#Задание4
list1=(4,5,5,1,2,3,4,8,1)
def slicer(x,el):
    newx=list(x)
    score=0
    for i in (range(len(x))):
        if el == x[i]:
            newx.pop(i)
            newx=tuple(newx)
            return newx
            break
        else:
            score+=1
    if score>0:
        return x
print(slicer(list1,10))