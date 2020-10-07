string=input()
substr=input()
if substr in string:
	print("String contains substring at index",string.find(substr))
else:
	print("not found")	