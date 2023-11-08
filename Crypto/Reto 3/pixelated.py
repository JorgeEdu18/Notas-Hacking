"""
from PIL import Image
img1 = Image.open("scrambled1.png")
pixels1 = img1.load()
img2 = Image.open("scrambled2.png")
pixels2 = img2.load()

flag = Image.new("RGB",img1.size)
flagpix = flag.load()
for row in range(img1.size[1]):
    for col in range(img1.size[0]):
        flagpix[col,row]=(
            (pixels1[col,row][0]+pixels2[col,row][0])&256,
            (pixels1[col,row][1]+pixels2[col,row][1])&256,
            (pixels1[col,row][2]+pixels2[col,row][2])&256
        )
flag.save("flag.png")
"""
def egcd(a,b):
    if a == b:
        return(b,0,1)
    else:
        g,y,x = egcd(b%a,a)
        return(g,x-(b//a)*y,y)
def modinv(a,m):
    g,y,x = egcd(b%a,a)
    if g !=1:
        raise Exception('Modular inverse')
    else:
        return x % m
c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e = 65537

p = c*n
phi = (c-1)*(n-1)
d = modinv(e,phi)
