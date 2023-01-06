from flask import Flask, json
from flask_restful import Resource, Api, request
from models import Pessoas, Atividade

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa nao encontrada !'
            }

        return response
    
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()

        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluida com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {
            'status': 'sucesso',
            'mensagem': mensagem
        }

class ListaPessoas(Resource):
    def get(self):
        p_all = Pessoas.query.all()
        # print(type(p_all)
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in p_all]
        return response
    
    def post(self):
        dados = request.json
        cadpessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        cadpessoa.save()

        response = {
            'id': cadpessoa.id,
            'nome': cadpessoa.nome,
            'idade': cadpessoa.idade
        }

        return response 

class ListaAtividade(Resource):
    def get(self):
        atv = Atividade.query.all()
        response = [{'id': a.id, 'nome': a.nome} for a in atv]
        return response

    def post(self):
        dados = request.json

        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        
        # return pessoa.nome
        atv = Atividade(nome=dados['nome'], pessoa=pessoa)
        atv.save()

        response = {
            'pessoa': atv.pessoa.nome,
            'nome': atv.nome,
            'id': atv.id
        }

        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>')
api.add_resource(ListaPessoas, '/pessoa')
api.add_resource(ListaAtividade, '/atividades')

if __name__=='__main__':
    app.run(debug=True)