from sqlalchemy.orm import scoped_session
from modelos.modelos import Produto

class ProdutoDAO:
    def __init__(self, session: scoped_session):
        self.session = session

    def criar(self, produto):
        self.session.add(produto)
        self.session.commit()

    def buscar_por_id(self, id_produto: int):
        return self.session.query(Produto).filter_by(id_produto=id_produto).first()

    def listar_produtos(self):
        return self.session.query(Produto).all()

    def atualizar_preco(self, id_produto: int, novo_preco: float):
        produto = self.buscar_por_id(id_produto)
        if produto:
            produto.preco = novo_preco
            self.session.commit()
            return produto
        return None

    def deletar(self, id_produto: int):
        produto = self.buscar_por_id(id_produto)
        if produto:
            self.session.delete(produto)
            self.session.commit()
            return True
        return False