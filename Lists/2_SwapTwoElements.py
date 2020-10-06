OrignalList=[]

try:
	

	while True:
		op=int(input("1-add element in list 2-interchancge elements, display and Exit "))

		if op==1:
				ele = int(input("enter elem to enter ")) 
				OrignalList.append(ele)               
				print(OrignalList)
		elif op==2:
			if len(OrignalList) ==0:
				print("List is empty")
			elif len(OrignalList)==1:
				print("There's just one element.. I don't think you need to swap")
			else:
				a=input(("Enter Position of 1st element you would like to swap [Start positon count with 0 ] "))
				b=input(("Enter Position of 2nd element you would like to swap [Start positon count with 0 ] "))
				if (a>len(OrignalList)-1) or (b>len(OrignalList)-1) or (a<0) or (b<0):
					print("Please enter correct position values ") 
				else:
					OrignalList[a], OrignalList[b]= OrignalList[b],OrignalList[a]
					print(OrignalList)
					break;
		else:
			print("Wrong input")

except ValueError:
	print("Enter number only ")