"""
###########
# Strings #
###########

Tipo de dados que a variavel recebe
String - Dados alfacaracteres, podem ser letras, simbolos ou numeros.
"""

a = "Lucas"
b = "Mariano"

concatenar = a + " " + b

my_string = "O rato roeu a roupa do rei de Roma"

# concatenar = a + " " + b + "\n"

# tamanho = len(concatenar) #Função len() conta a quantidade de caracteres que contem a string, no caso informa o tamanho da mesma

# print(tamanho)

# print(a[2]) # posso percorer a string e informar a posição que eu quero que seja retornado

# print(b[0:5]) # posso exibir um intervalo, informando a posição inicial e a final, que será até esse posição que sera retornado.

# print(concatenar.lower()) # posso usar a função lower() para deixar todos os caracteres em minusculos

# print(concatenar.upper()) # posso usar a função upper() para deixar todos os caracteres em MAISCULOS

# print(concatenar.strip()) # Remove caracteres expeciais como o \n usado para quebrar linha

# print(concatenar.split()) # Remove os espaços da string e transforma em um array, porém você poder passar uma caracter para a função remover também

#busca = my_string.find("rei") # Função find() usado para localizar a string e retornar a posição da mesma.
#print(busca)

print(my_string.replace("o rei", "a rainha")) #Função replace() usado para substituir uma palavra dentro da string, 1º argumento é quem será substituido o 2º argumento será a novo palavra que vai ficar no lugar




