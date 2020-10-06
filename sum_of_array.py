arr=list(map(int,input().strip().split())
sum=0
for i in range(0,len(arr)):
    sum=sum+arr[i]
print("sum of numbers of the array: ",end=" ")
print(sum)
