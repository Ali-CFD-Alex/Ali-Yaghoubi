# https://github.com/Ali-CFD-Alex
bits=input("Bit vared konid (0-1) : ")
data=list(bits)
i=0
newString = [];
while(i<len(data)):
  if(data[i]=='1'):
      newString.insert(i,'10')
  if(data[i]=='0'):
      newString.insert(i,'01')
  i+=1
output=''
output=''.join(newString)
output='11'+output+'00'
print("{} {}".format("Stuffing Message :",output))