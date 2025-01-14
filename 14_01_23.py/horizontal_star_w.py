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
"""
n=int(input("Enter the number :"))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print("* ", end=" ")
    print("")
    
for i in range(2,n+1):
    for j in range(i):
        print("* ", end=" ")
    print("")
"""

"""
n=int(input("Enter the number :"))

i=n
while(i>0):
    j=1
    while(j<=i):
        print("* ", end=" ")
        j+=1
    print("")
    i-=1
i=2
while(i<=n):
    j=0
    while(j<i):
        print("* ", end=" ")
        j+=1
    print("")
    i+=1
"""

#by using single while loop

n = int(input("Enter the number: "))
i=1
while i<=n*2+1:
    if i<=n:
        j=n-i+1
    else:
        j=i-n+1
    k=0
    while(k<j):
        print("* ", end=" ")
        k+=1
    print("")

    i+=1
    
