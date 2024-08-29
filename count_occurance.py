myList =[2,3,4,5,2,6,45,34,756,35456,77777,83,6734,1,2,77777]

myList.sort()

print(myList)
cntr=0
for i in range(len(myList)):
  if i==0 or (i!=0 and myList[i]!=myList[i-1]):
    print(f"{myList[i]}  Came  {myList.count(myList[i])} times")
  
  
