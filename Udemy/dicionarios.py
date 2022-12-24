"""
####################################
# DICIONARIOS (ARRAY INTERATIVOS ) #
####################################

Lista - conhecidos como array/vetores, são  basicamente uma variavel que tem varios espaços dentro para ser utilizado para armazenar informações/dados.
Podem ser de numeros, texto ou com os dois.

Esses Array interativos podemos colocar um chave e associar um dado ao mesmo.


"""

meu_dicio = {"A": "AMEIXA", "B": "BOLA", "C": "CACHORRO"}

#usando o for para percorrer todo o dicionario
# for chave in meu_dicio:
    # print(chave) # dessa forma vamos exibir somente a chave associativa ao item cadastro para a mesma
    # print(chave +" : "+meu_dicio[chave]) # dessa forma vamos exibir a chave e o item associado a mesma

#usando o metodo items para 
for i in meu_dicio.items():
    print(i)