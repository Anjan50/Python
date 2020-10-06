OrignalList=[]

try:
	

	while True:
		op=int(input("1-add element in list 2-Remove Nth occurence of word , display and Exit "))

		if op==1:
				ele = (input("enter word ")) 
				OrignalList.append(ele)               
				print(OrignalList)
		elif op==2:
			if len(OrignalList) ==0:
				print("List is empty ")
			else:
				word=input(("Enter word you want to remove "))
				N=int(input("Enter the Nth occurence the word u want to remove "))
				if word in OrignalList:
					c=[i for i, n in enumerate(OrignalList) if n == word][N-1]
					OrignalList.pop(c)
					print(OrignalList)
				else:
					print("The word you said doesn't exist in the list")
				
		else:
			print("Wrong input")

except ValueError:
	print("Enter number only ")

except IndexError:
	print("The Value You enterd for N is out of range ")