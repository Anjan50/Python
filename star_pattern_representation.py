"""

Make a pattern like below

   *  
  ***
 *****
*******
"""

length_star=7

for i in range(1,length_star+1,2):
    num=length_star-i
    print(int(num/2)*" ",end="")
    print(i*"*",end="")
    print(int(num/2)*" ",end="")
    print("\n",end='')


