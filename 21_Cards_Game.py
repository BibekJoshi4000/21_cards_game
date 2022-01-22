print("""		Welcome to 21 numbers Game.

User is requested to chose a single number and type the name of the row where it exist. Play correctly and you will see the magic""")
a=[x for x in range(1,8)]
b=[x for x in range (8,15)]
c=[x for x in range(14,22)]
for g in range (3):
	print("A=",a,"\n","B=",b,"\n","C=",c)
	z=input("Enter the name of the row where your number exists: ")
	if z =="a":
		d=b+a+c
	if z =="b":
		d=a+b+c
	if z=="c":
		d=b+c+a
	del a[:]
	del b[:]
	del c[:]
	for i in range(0,20,3):
		a.append(d[i])
	for i in range (1,20,3):
		b.append(d[i])
	for i in range (2,20,3):
		c.append(d[i])
print("The no. you are thinking is",d[10])
print("Thank you for playing")
exit=input("")
