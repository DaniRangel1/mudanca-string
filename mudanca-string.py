print("Inverta Caracteres de uma palavra")
string_original = input("escreva qualquer coisa aqui: ")
lista_caracteres = list(string_original)
tamanho =len(string_original)
for i in range(tamanho // 2):
    lista_caracteres[i], lista_caracteres[tamanho - i - 1] = lista_caracteres[tamanho - i - 1], \
    lista_caracteres[i]
string_invertida = "".join(lista_caracteres)
print(string_invertida)
