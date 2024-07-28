from flask_restful import Resource
from flask import jsonify, request
from models.heladeria import Heladeria 

class VentaResource(Resource):
    def __init__(self):
        self.heladeria = Heladeria() 

    def post(self, id):
        try:
            mensaje = self.heladeria.vender(id)
            return jsonify({'mensaje': mensaje})
        except ValueError as ve:
            return {'error': str(ve)}, 400
        except Exception as e:
            return {'error': str(e)}, 500
