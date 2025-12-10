from flask import *
from dao.banco import *
from dao.usuarioDAO import *

app = Flask(__name__)
app.secret_key = 'HGF431kSD&'

init_db()