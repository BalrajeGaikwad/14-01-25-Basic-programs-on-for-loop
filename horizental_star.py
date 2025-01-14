"""

*  *  *  *  *  *  
*  *  *  *  *
*  *  *  *
*  *  *
*  *
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
*  *  *  *  *  *

"""

"""n=int(input("Enter the number :"))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print("* ", end=" ")
    print("")
    
for i in range(2,n+1):
    for j in range(i):
        print("* ", end=" ")
    print("")
"""
n = int(input("Enter the count :- "))

for i in range(1, n * 2):
    if i <= n:
        j = n - i + 1
    else:
        j = i - n + 1
    for k in range(j):
        print("* ", end=" ")
    print("")
    