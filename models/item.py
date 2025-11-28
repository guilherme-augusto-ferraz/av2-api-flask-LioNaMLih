from database import db

class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, default=1)
    preco = db.Column(db.Float, default=0.0)
    comprado = db.Column(db.Boolean, default=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def para_dicionario(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco,
            "comprado": self.comprado
        }