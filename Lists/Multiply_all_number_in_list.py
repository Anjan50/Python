def mul_list(lst):

	result=1

	for i in lst:
		result=result*i

	return result

print("Enter the no of elements in list :")
n =int(input())
lst=[]
for i in range(n):
	lst.append(int(input()))

final_result = mul_list(lst)

print(final_result)
