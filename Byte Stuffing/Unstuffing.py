# https://github.com/Ali-CFD-Alex
class bcolors:
    BLUE = '\033[94m'
    ENDC = '\033[0m'
print(f"{bcolors.BLUE}Matn vared konid : {bcolors.ENDC}")

# daryaft payam
m=input()
# Daryaft DLE
print("DLE vared konid : ")
dle = input()
# Daryaft STX
print("STX vared konid : ")
stx = input()
# Daryaft ETX
print("ETX vared konid : ")
etx = input()
# Hazf khod matn DLE agar dar payam vojod dashte bashad
m=m.replace(dle+dle, dle)
# Hazf kardan DLE STX be aval payam
m = m.replace(dle+stx,"")
# Hazf kardan DLE ETX be akhar payam
m = m.replace(dle+etx,"")

# Namayesh
print("{} {}".format("Stuffing Message :",m))
