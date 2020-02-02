list1=['c','bb','aaaa','eee']
#--------normal sorting----------
list1.sort()
print(list1)
#-------sorting using length---------
list1.sort(key=len)
print(list1)
#----------normal sorting---------
list2=[[1,5],[3,9],[2,15]]
list2.sort()
print(list2)
#---------sorting using second element-----------
def secondele(a):
    return a[1]
list2.sort(key=secondele)
print(list2)
