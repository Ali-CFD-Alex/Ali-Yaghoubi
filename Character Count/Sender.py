# https://github.com/Ali-CFD-Alex
# daryaft tedad frame ha baraye ijad arraye
n=int(input("Tedad Frame ha (int) : "))
l=[]
l2=[]
# Halghe baraye daryaft mohtavaye har frame
for i in range(0,n):
  x=input("{} {} {} ".format("Matn Frame", i+1, ":"))
  # Ezafe kardan matn be arraye l
  l.append(x)
  # Ezafe kardan tol payam +1 braye ghaleb bandidar samt girande
  l2.append(len(x)+1)

sender=''
# halghe baraye tarkib kardan tol payam va khod payam
for i in range(0,n):
    sender+= str(l2[i])+l[i]
print("{} {}".format("Payam :",sender))