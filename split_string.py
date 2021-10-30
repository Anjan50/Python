def split_string(string):
	list_string = string.split(' ')
	return list_string
def join_string(list_string):
	string = '-'.join(list_string)
	return string
if __name__ == '__main__':
	string = 'I am a boy.'
	list_string = split_string(string)
	print(list_string)
	new_string = join_string(list_string)
	print(new_string)
