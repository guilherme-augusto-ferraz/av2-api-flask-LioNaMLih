from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from models.item import Item

item_bp = Blueprint('itens', __name__)

@item_bp.route('/itens', methods=['POST'])
@jwt_required()
def adicionar_item():
    usuario_id = get_jwt_identity()
    dados = request.get_json()

    if 'nome' not in dados:
        return jsonify({"mensagem": "O campo 'nome' é obrigatório"}), 400

    novo_item = Item(
        nome=dados['nome'],
        quantidade=dados.get('quantidade', 1),
        preco=dados.get('preco', 0.0),
        usuario_id=usuario_id
    )
    db.session.add(novo_item)
    db.session.commit()

    return jsonify(novo_item.para_dicionario()), 201

@item_bp.route('/itens', methods=['GET'])
@jwt_required()
def listar_itens():
    usuario_id = get_jwt_identity()
    itens = Item.query.filter_by(usuario_id=usuario_id).all()
    return jsonify([item.para_dicionario() for item in itens]), 200

@item_bp.route('/itens/<int:id>', methods=['PUT'])
@jwt_required()
def atualizar_item(id):
    usuario_id = get_jwt_identity()
    item = Item.query.filter_by(id=id, usuario_id=usuario_id).first()

    if not item:
        return jsonify({"mensagem": "Item não encontrado"}), 404

    dados = request.get_json()
    if 'nome' in dados: item.nome = dados['nome']
    if 'quantidade' in dados: item.quantidade = dados['quantidade']
    if 'comprado' in dados: item.comprado = dados['comprado']
    if 'preco' in dados: item.preco = dados['preco']

    db.session.commit()
    return jsonify(item.para_dicionario())

@item_bp.route('/itens/<int:id>', methods=['DELETE'])
@jwt_required()
def deletar_item(id):
    usuario_id = get_jwt_identity()
    item = Item.query.filter_by(id=id, usuario_id=usuario_id).first()

    if not item:
        return jsonify({"mensagem": "Item não encontrado"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"mensagem": "Item removido com sucesso"})