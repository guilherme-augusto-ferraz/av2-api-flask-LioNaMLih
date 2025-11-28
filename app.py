from flask import Flask
from database import db
from flask_jwt_extended import JWTManager
from routes.item_routes import item_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_compras.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'chave-super-secreta-do-trabalho'

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(item_bp)
app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return "API de Lista de Compras rodando!", 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)