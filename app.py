from flask import Flask, render_template, request, abort, jsonify
import math

app = Flask(__name__)

# NOSSA "BASE DE DADOS" EM MEMÓRIA
# Uma lista de dicionários
PRODUTOS = [
    {"id": 1, "nome": "Notebook Gamer X", "preco": 5200},
    {"id": 2, "nome": "Mouse sem Fio", "preco": 150},
    {"id": 3, "nome": "Teclado Mecânico RGB", "preco": 350},
    {"id": 4, "nome": "Monitor 27 polegadas", "preco": 150},
    {"id": 5, "nome": "SSD 512GB", "preco": 10},
    {"id": 6, "nome": "Headphones RGB Led", "preco": 450},
    {"id": 7, "nome": "Teclado Mecânico sem fio", "preco": 250},
    {"id": 8, "nome": "Gabinete com led", "preco": 130},
]

@app.route('/api/buscar-produto', methods=['POST'])
def buscar_produto():
    dados = request.get_json()
    nome_produto = dados.get('nome', '').lower()
    
    # Busca na nossa lista de dicionários
    resultado = [p for p in PRODUTOS if nome_produto in p['nome'].lower()]
    return jsonify({'produtos_encontrados':resultado})

@app.route('/produto/<int:produto_id>')
def detalhe_produto(produto_id):
    produto_encontrado - None
    # Busca pelo produto na lista ( performance 0(n) )
    for produto in PRODUTOS:
        if produto["id"] == produto_id:
            produto_encontrado = produto
            break
    if produto_encontrado is None:
        abort(404) # Item não encontrado

    return render_template('detalhe_produto.html', produto=produto_encontrado)

@app.route('/produtos-paginados')
def listar_produtos_paginados():
    page = request.args.get('page',1, type=int)
    per_page = 5 # Itens por página

    # Lógica da Paginação
    start = (page - 1) * per_page
    end = start + per_page
    total_pages = math.ceil(len(PRODUTOS)/per_page)

    # Fatiando a lista para pegar apenas os itens da página atual
    produtos_da_pagina = PRODUTOS[start:end]

    return render_template('produtos_paginados.html', produtos = produtos_da_pagina, page = page, total_pages = total_pages)

@app.route('/produtos')
def listar_produtos():
    return render_template('produtos.html', produtos=PRODUTOS)

@app.errorhandler(404)
def pagina_nao_encontrada():
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)