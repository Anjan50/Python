
Numbers=[]

def Curated(Numbers):
	pos,neg,zero=0,0,0
	for i in range(len(Numbers)):
		if (Numbers[i]==0):
			zero +=1
		elif(Numbers[i]>0):
			pos +=1
		else:
			neg +=1

	return pos,neg,zero;




while True:
	a=int(input("Enter 1- to add element 2-To get number of positive and negative and exit "))
	if a==1:
		ele=int(input("Enter the element "))
		Numbers.append(ele)

	elif a==2:
		pos,neg,zero=Curated(Numbers)
		print("+ve ",pos , " the -ves ",neg," the zeros", zero)
		break
	else:
		print("Wrong input ")

