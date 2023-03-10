from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id': 0, 'nome': 'Rafael', 'habilidades': ['Python', 'Flask']},
    {'id': 1, 'nome': 'Moreira', 'habilidades': ['Python', 'Django']}
    
]

# devolve um desenvolvedor pelo id, também alterar e deleta
@app.route("/dev/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor ID {} nao existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}    
        return jsonify(response)
    
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem':'Registro Excluido !!'})

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor

@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)

        return jsonify(desenvolvedores[posicao])
        # return jsonify({'status': 'sucesso', 'mensagem': 'Registro Inserido !'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)