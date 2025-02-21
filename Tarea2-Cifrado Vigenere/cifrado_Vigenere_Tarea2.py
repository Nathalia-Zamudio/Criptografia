A = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

diccionario = {A[i]: i for i in range(len(A))}

frase = input("Ingrese la frase a cifrar:_").upper()
clave = input("Ingrese la clave:_").upper()
codigo = []
cifrado = []

clave = ''.join([c for c in clave if c in diccionario])

clave_expandida = ''
clave_index = 0
for letra in frase:
    if letra in diccionario:
        clave_expandida += clave[clave_index % len(clave)]
        clave_index += 1
    else:
        clave_expandida += letra  

for i, letra in enumerate(frase):
    if letra in diccionario:
        desplazamiento = diccionario[clave_expandida[i]]
        codigo.append((diccionario[letra] + desplazamiento) % len(A))
    else:
        codigo.append(letra)

for i in codigo:
    if isinstance(i, int):
        cifrado.append(A[i])
    else:
        cifrado.append(i)

print(f"El cifrado es: {''.join(cifrado)}")