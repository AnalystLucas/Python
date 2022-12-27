from models import Pessoas, db_session

# Insere dados na tabela pessoas
def insere_pessoas():
    pessoa = Pessoas(nome='Moreira', idade=25)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela pessoas
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)   
    pessoa = Pessoas.query.filter_by(nome='Moreira').first()
    # print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Moreira').first()
    pessoa.nome = 'Lucas Moreira'
    pessoa.save()

#Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lucas Moreira').first()
    pessoa.delete()

if __name__=='__main__':
    # insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    consulta_pessoas()
