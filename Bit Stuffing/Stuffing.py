# https://github.com/Ali-CFD-Alex
bitstring=input("Bit vared konid (0-1) : ")
data=list(bitstring)
i=0
counter=0
while(i<len(data)):
  if(data[i]=='1'):
      counter+=1
  else: counter=0
  if(counter==5):
    data.insert(i+1,'0')
    counter=0
  i+=1
output=''
output=''.join(data)
output='01111110'+output+'01111110'
print("{} {}".format("Stuffing Message :",output))