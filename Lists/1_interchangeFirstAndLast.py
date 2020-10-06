OrignalList=[]

try:
	

	while True:
		op=int(input("1-add element in list 2-interchancge, display and Exit "))

		if op==1:
				ele = int(input("enter elem to enter ")) 
				OrignalList.append(ele)               
				print(OrignalList)
		elif op==2:
			if len(OrignalList) ==0:
				print("List is empty")
			else:
				OrignalList[len(OrignalList)-1], OrignalList[0]= OrignalList[0],OrignalList[len(OrignalList)-1]
				print(OrignalList)
				break;
		else:
			print("Wrong input")

except ValueError:
	print("Enter number only ")