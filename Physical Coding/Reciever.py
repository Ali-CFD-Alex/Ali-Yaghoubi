# https://github.com/Ali-CFD-Alex
bits=input("Bit vared konid (0-1) : ")
bits = bits[2:-2]
bits = [bits[index : index + 2] for index in range(0, len(bits), 2)]
i=0
newString = [];
while(i<len(bits)):
  if(bits[i]=='10'):
      newString.insert(i,'1')
  if(bits[i]=='01'):
      newString.insert(i,'0')
  i+=1
output=''
output=''.join(newString)
print("{} {}".format("Unstuffing Message :",output))