n=input()
a=0
b=0
for i in n:
	if i.isalpha():
		a=a+1
	elif i.isnumeric():
		b=b+1
if a+b==len(n) and a>0 and b>0:
	print('yes')
else :
		print('no')
