#1) print the numbers fro 0 to 100
print("print the numbers from 0 to 100")
for i in range(1,101):
    print(i,end=" ")


print("__________________________________________\n")


#2)  print the numbers from 100 to 1
print("print the numbers from 100 to 1")
for i in range(100,0,-1):
    print(i, end=" ")



print("\n")
#3) print all odd nmbers from the 1 to 100
print("print all odd nmbers from the 1 to 100")
for i in range(1,101):
    if i%2!=0:
        print(i, end=" ")

print("\n")
#4) print all odd nmbers from the 100 to 0
print("print all odd nmbers from the 100 to 0")
for i in range(100,0,-1):
    if i%2!=0:
        print(i ,end=" ")

