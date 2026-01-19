from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    email = Column(String, primary_key=True)
    nome = Column(String)
    senha = Column(String)

    def __repr__(self):
        return f"<Usuario(email='{self.email}', nome='{self.nome}')>"


class Produto(Base):
    __tablename__ = 'produtos'

    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nomep = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    descricao = Column(String)

    def __repr__(self):
        return f"<Produto(id_produto={self.id_produto}, nomep='{self.nomep}', preco={self.preco}, descricao={self.descricao})>"
