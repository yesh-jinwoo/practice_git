num=input("Enter the Number:")

result=[]

i=0
while i<len(num):
    if i<len(num)-1 and int(num[i])+int(num[i+1])==10:
        i+=2
    else:
        result.append(num[i])
        i+=1

print(f"\"{''.join(result)}\"")