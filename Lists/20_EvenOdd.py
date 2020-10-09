
Numbers=[]

def Curated(Numbers):
	odd,eve=0,0
	for i in range(len(Numbers)):
		if (Numbers[i]%2==0):
			eve +=1
		else:
			odd +=1

	return odd,eve;




while True:
	a=int(input("Enter 1- to add element 2-To get number of positive and negative and exit "))
	if a==1:
		ele=int(input("Enter the element "))
		Numbers.append(ele)

	elif a==2:
		odd,eve=Curated(Numbers)
		print("odd ",odd ," Evens ", eve)
		break;
	else:
		print("Wrogn input ")

