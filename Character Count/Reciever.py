# https://github.com/Ali-CFD-Alex
data=input("Matn ra vared konid : ")
i=0
inv=0
while(i<len(data)):
    if(data[i].isnumeric()==True):
        print(data[i+1:int(data[i])+i])
        i+=int(data[i])