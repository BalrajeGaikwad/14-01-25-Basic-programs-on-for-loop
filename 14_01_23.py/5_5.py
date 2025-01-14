"""n=int(input("Enter the count :- "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("* ", end=" ")
    print("")
"""
n=int(input("Enter the number :"))
i=1
while(i<=n):
    j=1
    while(j<=n):
        print("* ", end=" ")
        j+=1
    print("")
    i+=1


