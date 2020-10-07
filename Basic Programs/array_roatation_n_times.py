
def leftRotate(arr, d, n): 
	for i in range(gcd(d,n)): 
		temp = arr[i] 
		j = i 
		while 1: 
			k = j + d 
			if k >= n: 
				k = k - n 
			if k == i: 
				break
			arr[j] = arr[k] 
			j = k 
		arr[j] = temp 


def printArray(arr, size): 
	for i in range(size): 
		print ("%d" % arr[i], end=" ") 

def gcd(a, b): 
	if b == 0: 
		return a; 
	else: 
		return gcd(b, a%b) 

n=int(input())
arr=[]
for i in range(n):
    t=int(input())
    arr.append(t)
nos=int(input())
leftRotate(arr, nos, n) 
printArray(arr, n) 


