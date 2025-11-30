from flask import Flask, render_template
from controllers.produto_controller import ProdutoController
from models.db import init_db

app = Flask(__name__)

# o init inicializa o banco SQLite na primeira execução
init_db()

@app.route('/api/buscar-produto', methods=['POST'])
def buscar_produto():
    return ProdutoController.buscar_produto()

@app.route('/produto/<int:produto_id>')
def detalhe_produto(produto_id):
    return ProdutoController.detalhe_produto(produto_id)

@app.route('/produtos-paginados')
def produtos_paginados():
    return ProdutoController.produtos_paginados()

@app.route('/produtos')
def listar_produtos():
    return ProdutoController.listar_produtos()

@app.route('/inserir-produto', methods=['POST'])
def inserir_produto():
    return ProdutoController.inserir_produto()

@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True, port=(5003))
