from flask import jsonify

def register_routes(app):
    @app.route('/')
    def index():
        return jsonify({"message": "API CRM Delivery ativa com sucesso!"})