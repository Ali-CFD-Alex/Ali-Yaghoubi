# https://github.com/Ali-CFD-Alex
class bcolors:
    BLUE = '\033[94m'
    ENDC = '\033[0m'
print(f"{bcolors.BLUE}Bit vared konid (0 ya 1) : {bcolors.ENDC}")


# Daryafet bit ha
bitstring=input()
# tabdil reshte bit ha be array az bit ha
data=list(bitstring)
# i baraye shomaresh arraye va ezafe kardan 0 bad az 5 yek motavali 
i=0
# c baraye shomaresh 5 yek motavali
c=0
# halghe baraye peymayesh tol arraye
while(i<len(data)):
  # shart ke agar 1 bod be c yek vahed ezafe konim ta betavanim tashkhis bedahim ke aya 5 yek motavali darim ya kheyr
  if(data[i]=='1'):
      c+=1
  # agar bit 1 nabood meghdar c reset mikonim baraye shomaresh az aval
  else: c=0
  # shart ke agar c barabar 5 bod yani ma 5 ta yek motavali darim
  if(c==5):
    # ezafe kardan 0 bad az 5 yek motavali (i+1 baraye ezafe kardan 0 bad az 5 yek motavali)
    data.insert(i+1,'0')
    # reset kardan c
    c=0
  # ezafe kardan meghdar i ta naghz shart while
  i+=1

x=''
# tabdil arraye be string jahat namayesh
x=''.join(data)
print("{} {}".format("Stuffing Message :",x))