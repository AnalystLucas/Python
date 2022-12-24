"""
###########
# Funções #
###########

Funções é um conjunto de instruções defido pelo programador ou pode também já ser funções nativas, aquela que já esta dentro do escopo da linguagem

def - Palavra chave para criar ma função em python
def nome_funcao() - nome_funcao() é como você pode chamar aquela função
def nome_funcao(argumentos) é usada para que seja definido os argumentos utilizados para aquela função

observação quando utilizamos função (def), devemos sempre utilizar após o nome da mesma o simbolo de "()"

"""
def soma(x , y): # essa função que criamos, vai receber 2 argumentos e será feito a soma dos mesmos.
    # print(x + y) # aqui estamos passando para a função que sejá printado ( exibir a informação da soma)
    return x + y   # Normalmente em funções usamos a palavra reservada Return, ela vai retorna a soma e não será exibido mais a mensagem igual o print estava fazendo, dessa maneira podemos trabalhar outras informações apartir do retorno de uma função

def multiplicacao(x, y):
    return x * y
s = soma(2, 2) # Quando trabalhos com return é necessário armazenar a informação em uma variavel e depois exibir em outro momento do codigo.
m = multiplicacao(3, 5)

print(soma(s, m)) # trabalhando com recursividade, a função soma esta recebendo ela mesmo e mais a multiplicação, através das variaveis, s = soma, m = multiplicação

