"""
######################
# Manipular Arquivos #
######################

para Manipular arquivos precisamos usar a função open

a função tem alguns argumentos que podem ser utilizado com a função

r  - somente leitura
w  - escrita (caso o arquivo já exista, ele será apagado e um novo arquivo vazio será criado)
a  - leitura e escrita (adiciona o novo conteudo ao fim do arquivo)
r+ - leitura e escrita
w+ - escrita (o modo w+, assim como o w, também apaga o conteudo anterior do arquivo)
a+ - leitura e escrita (abre o arquivo para atualização)

"""
# arquivo = open("arquivo.txt") # abrindo o arquivo e armazenando na variavel

# txt_comp = arquivo.read() # funcção read(), faz a leitura completa do arquivo e assim posso exibir o seu conteudo ou manipular.

# print(txt_comp)

# -*- coding: utf-8 -*-

# w = open("arquivo2.txt", "w") # usando o argumento w para criar um arquivo novo.

# w.write("Meu arquivo 2") # usando o arqumento 2 para escrever informação no arquivo 2.

# w.close() # fechando o arquivo que foi aberto

a = open("arquivo.txt", "a") # argumento usado para atualizar a informação do arquivo

a.write("Esse arquivo foi criado primeiro ! \n")

a.close()