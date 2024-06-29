#Задание1
list=[7,4,2,6,7,2,1]
def score(x):
    listend=[]
    per=round(len(x)/3)
    if sum(x)/len(x)>0:
        listend+=sorted(x[0:len(x) - per])
        listend+=x[len(x) - per:]
    else:
        listend+=sorted(x[0:len(x) - per*2])
        listend+=sorted(x[len(x) - per*2:],reverse=True)
    print(listend)
score(list)

#Задание2
import random
list=[]
for i in range(0,10):
    list.append(random.randint(1,12))
def score(x):
    print(f"Общее содержание {x}")
    new=int(input("Заменяемое число:"))
    new2 = int(input("Оценочное число:"))
    x[new]=new2
    if sum(x)/len(x)>=10.7:
        print(f"Стипендия предусмотрина")
    else:
        print(f"Стипендия не предусмотрина")
    print(sorted(x))
score(list)

#Задание 3
def bubble_sort(list1):
    end=0
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if (list1[j] > list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
                end+=1
    print(f"Кол-во повтарений {end}")
    return list1


list1 = [6, 2, 1, 3, 4, 5]
print(bubble_sort(list1))
