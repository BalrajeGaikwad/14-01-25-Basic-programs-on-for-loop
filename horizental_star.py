
n=int(input("Enter the number :"))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print("* ", end=" ")
    print("")
    
for i in range(2,n+1):
    for j in range(i):
        print("* ", end=" ")
    print("")

