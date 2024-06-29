# Задание1
list1=["+79999999999","+70000000000","+75555555555"]
list2=["5123","5128","3217"]
list3=[]
for i in range(len(max(list2,list1))):
    list3.append(f"{list1[i]}={list2[i]}")
print(sorted(list1))
print(sorted(list2))
print(list3)


list1=["С приветом по планетам","До центра земли и обратно","Идиот"]
list2=["1997","2018","2010"]
list3=[]
for i in range(len(max(list2,list1))):
    list3.append(f"{list1[i]}-{list2[i]}")
print(sorted(list1))
print(sorted(list2))
print(list3)