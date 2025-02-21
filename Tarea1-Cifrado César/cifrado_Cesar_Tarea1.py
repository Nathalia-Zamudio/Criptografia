A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

diccionario = {A[i]: i for i in range(len(A))}

frase = input("Ingrese la frase a cifrar:_")
frase = frase.upper()
k = int(input("Ingrese la llave:_"))
codigo = []
cifrado = []

for i in frase:
    if i in diccionario: 
        codigo.append((diccionario[i] + k) % len(A))
    else:
        codigo.append(i)  

for i in codigo:
    if isinstance(i, int): 
        cifrado.append(A[i])
    else:
        cifrado.append(i) 

print(f"El cifrado es: {''.join(cifrado)}")
