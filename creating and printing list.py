list1=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print("List of tuple before sorting : " + str(list1))
for i in range(0,len(list1)):
    for j in range(0,len(list1) -i-1):
        if(list1[j][-1]>list1[j+1][-1]):
            swap=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=swap
print("List of tuple after sorting:" +str(list1))                        
    