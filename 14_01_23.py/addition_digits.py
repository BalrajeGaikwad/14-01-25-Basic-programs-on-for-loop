num = int(input("Enter a number:- "))
sum= 0
while num > 0:
    sum += num % 10
    print("sum : ", sum)
    print("num before updating :- ",num)
    num = num // 10
    print("num : ",num)
print("sum of the digits is:-", sum)

    

