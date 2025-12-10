from sqlalchemy import create_engine #cria conexão com o bd
#scoped fornece uma sessão de bd segura para multiplas aplicações, sessionmaker define como as sessões serão criadas.
from sqlalchemy.orm import scoped_session, sessionmaker
#classe base onde os modelos (tabelas) são registrados
from modelos.modelos import Base

#engine conecta ao banco usuarios.db usando SQLite
#echo=true faz o SQLAlchemy imprimir no console todas as queries SQL executadas
engine = create_engine('sqlite:///usuarios.db', echo=True)

#Cria uma sessão vinculada ao engine.
#scoped_session garante que cada thread (ou requisição, em apps web) tenha sua própria sessão isolada.
Session = scoped_session(sessionmaker(bind=engine))


#cria todas as tabelas definidas nos modelos que herdam de Base
def init_db():
    Base.metadata.create_all(engine)
#Base.metadata.create_all(engine) lê os modelos e gera as tabelas no banco usuarios.db se elas ainda não existirem.


#Configura a conexão com um banco SQLite chamado usuarios.db.
#Cria uma fábrica de sessões para interagir com o banco.
#Define uma função init_db() que cria as tabelas baseadas nos modelos definidos.
##criar um para produtos;  verificar rotas esta bagunçado!