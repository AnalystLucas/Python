"""
##########################
# Tratamento de Excecoes #
##########################

Precisamos lidar com problemas que não seja erro de logica e outros tipos de erros que não codigo e etc.

"""
a = 2
b = 0

#Try seria tente, estamos dizendo pro programa tentar executar o codigo e se caso tiver erro vamos tratar

try:
    print(a/b) 
#Except seria exececao, caso tenha erro, vamos entrar na excecao do codigo e assim podemos tratar o mesmo
except:
    print("Não foi possivel realizar essa operação !")
