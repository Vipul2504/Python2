list1 = []
list2 = []

for i in range (1,11):
    list1.append(4*i)

for i in range (0,10):
    list2.append(list1[i]%4==0)
    
print("see whether at least one number is divisible by 5 in list 1 =>")
print(any(list2))

list3 = []
list4 = []

for i in range (1,21):
    list3.append(4*i-3)

for i in range (0,20):
    list4.append(list3[i]%2==1)
    
print("see whether at least one number is divisible by 2 in list 3 =>")
print(all(list4))