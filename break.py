#break
av=10
x=int(input("how many candies do you want"))
i=1
while i<=x:
    if i>av:
        print("out of stock")
        break
    print("candy")
    i+=1
print("bye")
