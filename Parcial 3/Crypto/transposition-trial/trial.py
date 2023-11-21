with open("message.txt") as fl:
    contenido = fl.read()

for i in range(0, len(contenido),3):
    chunk = contenido[i:i+3]
    a,b,c = chunk
    print(c + a + b, end="" )