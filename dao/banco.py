from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from modelos.modelos import Base

engine = create_engine('sqlite:///usuarios.db', echo=True)

Session = scoped_session(sessionmaker(bind=engine))

def init_db():
    Base.metadata.create_all(engine)




#Configura a conexão com um banco SQLite chamado usuarios.db.
#Cria uma fábrica de sessões para interagir com o banco.
#Define uma função init_db() que cria as tabelas baseadas nos modelos definidos.
##criar um para produtos;  verificar rotas esta bagunçado!