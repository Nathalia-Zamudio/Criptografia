A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

diccionario = {A[i]: i for i in range(len(A))}

frase = input("Ingrese la frase a cifrar:_")
frase = frase.upper()
k = int(input("Ingrese la llave:_"))
codigo = []
cifrado = []

# Convertir cada letra en su índice correspondiente
for i in frase:
    if i in diccionario:  # Si el carácter está en el diccionario, cifrarlo
        codigo.append((diccionario[i] + k) % len(A))
    else:
        codigo.append(i)  # Si es un espacio u otro carácter, mantenerlo igual

# Convertir los índices cifrados de nuevo a letras
for i in codigo:
    if isinstance(i, int):  # Si es un número, es una letra cifrada
        cifrado.append(A[i])
    else:
        cifrado.append(i)  # Si es un espacio, mantenerlo igual

print(f"El cifrado es: {''.join(cifrado)}")
