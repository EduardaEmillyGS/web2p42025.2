from flask import *
from dao.banco import *
from dao.produtoDAO import ProdutoDAO
from dao.usuarioDAO import *
from modelos.modelos import Produto

#INSTANCIANDO O OBJETO DO SERVIDOR FLASK
app = Flask(__name__)
app.secret_key = 'HGF431kSD&'

init_db()

@app.before_request
def pegar_sessao():
    g.session = Session()#ao criar a aplicaçao ele instancia um objeto de sessao para acesso controlado ao BD

@app.teardown_appcontext
def encerrar_sessao(exception=None):
    if exception:
        print(f"Erro durante a requisição: {exception}")
    Session.remove()

@app.route('/')
def abrir_home_page():
    return render_template('paginainicial.html')

@app.route('/menu', methods=['GET'])
def acessar_menu():
    return render_template('menu.html')


@app.route('/fazerlogin', methods=['POST', 'GET'])
def fazer_login():

    if request.method == 'GET' and 'login' in session:
        print("logado via link")
        return render_template('pglogado.html')

    if request.method == 'GET':
        return  render_template('login.html')

    login = request.form.get('loginusuario')
    senha = request.form.get('senhausuario')

    udao = UsuarioDAO(g.session)

    usuario = udao.autenticar(login, senha)
    if usuario:
        print(usuario)
        session['login'] = login
        print("logado via login")
        return render_template('pglogado.html')
    else:
        #aqui o usuario digitou o login ou senha errado
        msg = 'Usuário ou senha inválidos'
        return render_template('paginainicial.html', texto=msg)


@app.route('/cadastrar', methods=['GET','POST'])
def cadastrar():
    if request.method == 'GET':
        return render_template('paginacadastro.html')

    udao = UsuarioDAO(g.session)
    nome = request.form.get('nomeuser')
    email = request.form.get('email')
    senha = request.form.get('senha')
    confirma = request.form.get('confirmacao')

    if senha == confirma:
        udao.criar(Usuario(email=email, nome=nome, senha=senha))
        return render_template('login.html')
    else:
        msg = 'a senha e a confirmação de senha não são iguais'
        return render_template('paginacadastro.html', msg=msg)


@app.route('/listar')
def listar_usuarios():
    if 'login' in session:
        udao = UsuarioDAO(g.session)
        usuarios = udao.listar_usuarios()
        return render_template('listar.html',usuarios=usuarios)
    else:
        return render_template('paginainicial.html')

@app.route('/detalhes')
def mostrar_detalhes():
    if 'login' in session:
        print(session['login'])
        udao = UsuarioDAO(g.session)

        email = request.values.get('email')
        usuario = udao.buscar_por_email(email)

        if usuario:
            return render_template('detalhes.html', usuario=usuario)
        else:
            msg = 'usuário nao encontrado'
            return render_template('mensagemerro.html', msg=msg)
    else:
        return render_template('paginainicial.html')

@app.route('/cadastrarproduto', methods=['Get'])
def produto():
    if request.method == 'Get':
        return render_template('cadastrarproduto.html')

    uproduto = ProdutoDAO(g.session)
    nomep = request.form.get('nomep')
    id_produto = request.form.get('id_produto')
    preco = request.form.get('preco')

    if id_produto == int:
        uproduto.criar(Produto(id_produto=id_produto, nomep=nomep, preco=preco))
        return render_template('listarproduto.html')
    else:
        msg = 'produto invalido'
        return render_template('cadastrarproduto.html', msg=msg)



#end-point ou route (rota)
@app.route('/dados')
def pegar_dados():
    iid = request.values.get('id')
    nome_user = request.values.get('nome')
    if iid:
        print(iid) #era id alterei para resolver o erro que estava apresentando
    if nome_user:
        print(nome_user)
    return 'deu cerrtooo'

@app.route('/contato', methods=['GET'])
def contatos():
    return render_template('contato.html')

@app.route('/voltar', methods=['GET'])
def voltar():
    return render_template('paginainicial.html')

@app.route('/retorno', methods=['GET'])
def retorno():
    return render_template('pglogado.html')

@app.route('/logout')
def fazer_logout():
    #limpo o objeto session (dicionário)
    session.clear()
    return render_template('paginainicial.html')

#EXECUTANDO O SERVIDOR
if __name__ == '__main__':
    app.run(debug=True, port=5001)