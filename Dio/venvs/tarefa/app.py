from flask import Flask, request, json, jsonify

app = Flask(__name__)

tarefas = [
    {'id': 0, 'responsavel': 'Lucas', 'tarefa': 'inicializar tarefa', 'status': 'concluido'},
    {'id': 1, 'responsavel': 'Moreira', 'tarefa': 'criar metodo get', 'status': 'pendente'}
]

#Home da tarefa !
@app.route('/')
def inicializando():
    
    return "Bem vindo a Tarefa !"

#Listar todas as tarefas e criar tarefas
@app.route('/tarefa', methods=['GET', 'POST'])
def tarefas_rc():
    if request.method == 'GET':
        response = tarefas
    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        response = {'status':'sucesso', 'mensagem': 'Tarefa Criada !!'}

    return jsonify(response)

@app.route('/tarefa/<int:id>', methods=['PUT', 'DELETE', 'GET'])
def tarefa_rwd(id):
    if request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id]['status'] = dados['status']
        response = {'status': 'sucesso', 'mensagem': 'Alteração Realizada !'}
    
    elif request.method == 'GET':
        response = tarefas[id]
    
    elif request.method == 'DELETE':    
        tarefas.pop(id)
        response = {'status': 'sucesso', 'mensagem':'Registro deletado'}

    return  jsonify(response)
if __name__ == '__main__':
    app.run(debug=True)