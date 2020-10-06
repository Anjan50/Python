def SplitText(parts, text):
    partl = len(text)//parts
    rem = len(text)%parts
    l = []
    cnt = 0;
    for i in range(parts):
        thislen=partl
        if(rem>0):
            rem-=1
            thislen+=1
        l.append("")
        l[i]=text[cnt:cnt+thislen]
        cnt+=thislen
    return l

print("enter text")
text = input()
print("enter number")
num = int(input())
texts = SplitText(num,text)
for part in texts:
    print(part)
input()

            
    
