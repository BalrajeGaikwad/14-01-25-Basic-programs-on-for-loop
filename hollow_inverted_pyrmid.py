
"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

* * * * * 
 * * * * 
  * * * 
   * * 
    * 

"""
rows=5
for i in range(rows):
    print(" "*(rows-i-1), end="")
    print("* " *(i+1))

for i in range(rows,0,-1):
    print(" "* (rows-i) , end="")
    print("* "* i)
