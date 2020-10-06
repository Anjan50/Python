n=int(input())
lis=[int(input()) for i in range(n)]
outputlis=[]
cumsum=lis[0]
outputlis.append(lis[0])
for i in range(1,n):
    cumsum+=lis[i]
    outputlis.append(cumsum)   
print(outputlis)     


