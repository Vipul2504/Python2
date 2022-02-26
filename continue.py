#print all the number between 1-100 but not who divide by 3 5
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)
print("bye")
