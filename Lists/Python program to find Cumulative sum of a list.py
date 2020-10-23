def cum_sum(list):
  cum_list=[]
  length=len(list) 
  cum_list=[sum(list[0:x:1])for x in list]
  return cum_list


list=[1,2,3,4,5,6,7]
print(list)
print(cum_sum(list))

#Break a list into N chuncks
