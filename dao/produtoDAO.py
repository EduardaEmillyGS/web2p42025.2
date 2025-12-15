from sqlalchemy.orm import scoped_session
from modelos.modelos import Produto


class ProdutoDAO:
    #construtor da classe: instanciar um objeto, ele cria uma sessao
    def __init__(self, session: scoped_session):
        self.session = session

    def criar(self, produto):
        #adiciona um objeto/modelo no banco de dados
        self.session.add(produto)
        #autorizando modificações no banco/ gravando a alteração
        self.session.commit()

    def buscar_por_id(self, id_produto: int):
        return self.session.query(Produto).filter_by(id_produto=id_produto).first()

    def listar_produtos(self):
        return self.session.query(Produto).all()

    def atualizar_preco(self, id_produto: int, novo_preco: float):
        # atualiza o preço de um produto específico
        produto = self.buscar_por_id(id_produto)
        if produto:
            produto.preco = novo_preco
            self.session.commit()
            return produto
        return None

    def deletar(self, id_produto: int):
        # remove um produto do banco
        produto = self.buscar_por_id(id_produto)
        if produto:
            self.session.delete(produto)
            self.session.commit()
            return True
        return False