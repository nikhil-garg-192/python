nested_list = [[1, 2], [3, 4], [5, 6]]
newlist=[]

flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]


#above list comprehension is same as the code below
for sublist in nested_list: 
  for item in sublist:
     newlist.append(item)
     
print(newlist)  # Output: [1, 2, 3, 4, 5, 6]   