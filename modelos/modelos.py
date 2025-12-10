from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

#é um modelo que vai  representar uma tabela no BD
Base = declarative_base()
class Usuario(Base):
    __tablename__ = 'usuarios'

    email = Column(String, primary_key=True)
    nome = Column(String)
    senha = Column(String)

    def __repr__(self):
        return f"<Usuario(email='{self.email}', nome='{self.nome}')>"


#fazer outro model classe passagem no modelo
#alterar usuarios para passagen + novo usuario dao altera todos os usuarios para passagem funções de acorso com o modelo id, nome, preço
# + aplicação nos servidor exemplo:  udao = UsuarioDAO(g.session)  + htmml de listar e cadastrar produto/passagem criar uma rota para ligação
#importar passagem/produto no servidor "from DAO.passagemDAO import * "