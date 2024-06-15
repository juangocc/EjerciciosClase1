cadena = 'reconocer'

reverso = ""

for caracter in cadena:
    reverso = caracter + reverso

if reverso == cadena:
    print('palindromo')
else:
    print('no es palindromo')