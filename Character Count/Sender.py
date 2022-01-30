# https://github.com/Ali-CFD-Alex
n=int(input("Tedad Frame ha (int) : "))
l=[]
l2=[]
for i in range(0,n):
  x=input("{} {} {} ".format("Matn Frame", i+1, ":"))
  l.append(x)
  l2.append(len(x)+1)
sender=''
for i in range(0,n):
    sender+= str(l2[i])+l[i]
print("{} {}".format("Payam :",sender))