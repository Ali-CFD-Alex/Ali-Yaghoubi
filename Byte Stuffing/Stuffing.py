# https://github.com/Ali-CFD-Alex
def applyByteStuffing(flagbyte, escapebyte, payload):
    x = payload.replace (escapebyte, escapebyte*2)
    y = escapebyte+flagbyte
    return y + x + y
print("Byte vared konid (a-zA-Z) : ")
Byte=input().upper()
print("DLE vared konid : ")
DLE = input().upper()
print("Flag vared konid (stx-etx) : ")
Flag = input().upper()
output = applyByteStuffing(Flag,DLE,Byte)
print("{} {}".format("Stuffing Message :",output))
