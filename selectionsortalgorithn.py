#how to get input from shell
totalinput=int(input('enter the total numbers'))
list1=[int(input('Enter the value'))for i in range(totalinput)]
print(list1)



#minsort
'''
list1=[56,3,2,78,6,0]
for i in range(len(list1)-1):
    min_val=min(list1[i:])
    min_index=list1.index(min_val)
    list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)
'''
#maxsort
'''
list1=[56,3,2,78,6,0]
for i in range(len(list1)-1):
    min_val=max(list1[i:])
    min_index=list1.index(min_val)
    list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)
'''
#sorting for duplicate values
'''
list1=[56,3,2,78,6,0]
for i in range(len(list1)-1):
    min_val=min(list1[i:])
    min_index=list1.index(min_val,i)
    list1[i],list1[min_index]=list1[min_index],list1[i]
    print(list1)

'''
#sorting for duplicate values to reduce the loop
'''
list1=[56,3,2,78,6,0]
for i in range(len(list1)-1):
    min_val=min(list1[i:])
    min_index=list1.index(min_val,i)
    if list1[i]!=list1[min_index]:
        list1[i],list1[min_index]=list1[min_index],list1[i]
    print(list1)
'''



