from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from database import db
from models.usuario import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/registro', methods=['POST'])
def registrar():
    dados = request.get_json()

    if not dados or not dados.get('nome_usuario') or not dados.get('senha'):
        return jsonify({"mensagem": "Dados incompletos (nome_usuario e senha obrigatórios)"}), 400

    if Usuario.query.filter_by(nome_usuario=dados['nome_usuario']).first():
        return jsonify({"mensagem": "Nome de usuário já existe"}), 400

    novo_usuario = Usuario(nome_usuario=dados['nome_usuario'])
    novo_usuario.definir_senha(dados['senha'])

    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"mensagem": "Usuário criado com sucesso!"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    usuario = Usuario.query.filter_by(nome_usuario=dados.get('nome_usuario')).first()

    if usuario and usuario.verificar_senha(dados.get('senha')):

        token_acesso = create_access_token(identity=str(usuario.id))
        return jsonify(token_acesso=token_acesso), 200

    return jsonify({"mensagem": "Credenciais inválidas"}), 401