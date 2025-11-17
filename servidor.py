from flask import *
from utils.acesso_bd import*

#INSTANCIANDO O OBJETO DO SERVIDOR FLASK
app= Flask(__name__)
usuarios = [['diego','d@d','123'],['mariany','m@m','123'],['jose','j@j','123'],['rene','r@r','123']]

@app.route('/')
def abrir_home_page():
    return render_template('index.html')

@app.route('/fazerlogin', methods=['post'])
def fazer_login():

    login = request.form.get('loginusuario')
    senha = request.form.get('senhausuario')

    if verificar_login(usuarios, login, senha):
        return render_template('logado.html')
    else:
        # aqui o usuario digitou o login ou senha errado
        msg = 'usuario ou senha inválidos'
        return render_template('index.html', texto=msg)


@app.route('/cadastrar', methods=['GET','POST'])
def cadastrar():
    if request.method == 'GET':
        return render_template('paginacadastro.html')

    nome = request.form.get('nomeuser')
    email = request.form.get('email')
    senha = request.form.get('senha')
    confirma = request.form.get('confirmacao')

    if senha == confirma:
        global usuarios
        usuarios.append([nome, email, senha])
        return render_template('index.html')
    else:
        msg = 'a senha e a confirmação de senha não são iguais'
        return render_template('paginacadastro.html', msg=msg)


@app.route('/listar')
def listar_usuarios():
    return render_template('listar.html',usuarios=usuarios)

@app.route('/detalhes')
def mostrar_detalhes():
    email = request.values.get('email')
    usuario = buscar_usuario(usuarios, email) #simulando um banco de dados

    if usuario:
        return render_template('detalhes.html', usuario=usuario)
    msg = 'usuário nao encontrado'
    return render_template('mensagemerro.html', msg=msg)

#end-point ou route (rota)
@app.route('/dados')
def pegar_dados():
    id = request.values.get('id')
    nome_user = request.values.get('nome')
    if id:
        print(id)
    if nome_user:
        print(nome_user)
    return 'deu cerrtooo'


@app.route('/logout')
def fazer_logout():
    return render_template('index.html')

#EXECUTANDO O SERVIDOR
app.run()