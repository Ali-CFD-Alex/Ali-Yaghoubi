# https://github.com/Ali-CFD-Alex
def byteUnstuffing(flagbyte, escapebyte, payload):
    x = payload.replace(escapebyte*2, escapebyte)
    y = escapebyte+flagbyte
    return x.replace(y,'')
print("Byte vared konid (a-zA-Z) : ")
Byte=input().upper()
print("DLE vared konid : ")
DLE = input().upper()
print("Flag vared konid (stx-etx) : ")
Flag = input().upper()
output = byteUnstuffing(Flag,DLE,Byte)
print("{} {}".format("Untuffing Message :",output))
