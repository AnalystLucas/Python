from flask_restful import Resource

list_habilidades = ['Django','Java','Python','Flask','PHP']

class Habilidades(Resource):
    def get(self):
        return list_habilidades