# list1 = [23,49,67,29,12,1,5,76]
# list1.append(3)
# print(list1)
# list1.pop(3)
# print(list1)
# list1.insert(3,26)
# list1.extend([3,6,8,4])
# print(list1)    


# list=[]
# for i in range(0,10):
#     list.append(i)
# print(list)

# List2 = [['Geeks', 'For'] , ['Geeks']]
# print(List2[0][1])
# print(List2[1][0])

list = ['G','E','E','K','S','F','O','R','G','E','E','K','S']
slice_list = list[2:8]
print(slice_list)

# pre-defined point to end
# Sliced_List = list[5:]
# print("\nElements sliced from 5th "
#       "element till the end: ")
# print(Sliced_List)

list3 = [i for i in range(20) if i % 2 == 1]
print(list3)