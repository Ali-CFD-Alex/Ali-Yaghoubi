# https://github.com/Ali-CFD-Alex
class bcolors:
    BLUE = '\033[94m'
    ENDC = '\033[0m'
print(f"{bcolors.BLUE}Matni ke tavasot ferestande ijad shode ast ra copy konid !{bcolors.ENDC}")


data=input("Matn ra vared konid : ")
# i baraye ijad halghe
i=0
inv=0
while(i<len(data)):
    # Peyda kardan addad dar beyn matn
    if(data[i].isnumeric()==True):
        # namayesh matn az arraye khane i+1 ta mehgdar khane i+1
        # agar avalin adad 6 bashad baraye "Hello" dar arraye darim [6,H,e,l,l,o]
        # pas ma bayad az mogheyiat (index) avalin khane +1 ke mishavad haman 1 yani "H"
        # ta meghdar avalin khane yani 6 balaveye 1 (7 chon ke ta 7 chap konad vali khod khane 7 ro na agar 6 khali bod dar mesal o ra chap nemikard)
        print(data[i+1:int(data[i])+i])
        # rad shodan az in kalame va raftan be kalame baad
        i+=int(data[i])