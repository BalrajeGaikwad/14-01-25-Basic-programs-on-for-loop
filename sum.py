"""n=int(input("Enter the number : "))

d1=n//10000
print(d1)
d2=(n//1000)%10
print(d2)
d3=(n//100)%10
print(d3)
d4=(n//10)%10
print(d4)
d5=n%10
print(d5)


sum=d1+d2+d3+d4+d5
print(sum)
"""


num = int(input("Enter a number:- "))
sum= 0
while num > 0:
    sum += num % 10
    print("sum : ", sum)
    print("num before updating :- ",num)
    num = num // 10
    print("num : ",num)
print("sum of the digits is:-", sum)

    
