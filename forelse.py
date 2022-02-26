nums=[10,23,25,30,35,40,46,50]

for num in nums:

    if num % 9 ==0:
        print(num)
        break
else:
    print("not found")
