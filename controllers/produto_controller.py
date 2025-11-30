from flask import render_template, request, jsonify, abort
from models.produto_model import ProdutoModel
import math

class ProdutoController:

    @staticmethod
    def listar_produtos():
        produtos = ProdutoModel.listar_todos()
        return render_template("produtos.html", produtos=produtos)

    @staticmethod
    def detalhe_produto(produto_id):
        produto = ProdutoModel.buscar_por_id(produto_id)
        if not produto:
            abort(404)
        return render_template("detalhe_produto.html", produto=produto)

    @staticmethod
    def buscar_produto():
        dados = request.get_json()
        nome = dados.get("nome", "")
        produtos = ProdutoModel.buscar_por_nome(nome)
        return jsonify({"produtos_encontrados": [dict(p) for p in produtos]})

    @staticmethod
    def produtos_paginados():
        page = request.args.get("page", 1, type=int)
        per_page = 5
        offset = (page - 1) * per_page

        total = ProdutoModel.contar()
        produtos = ProdutoModel.listar_paginado(offset, per_page)

        total_pages = math.ceil(total / per_page)

        return render_template(
            "produtos_paginados.html",
            produtos=produtos,
            page=page,
            total_pages=total_pages
        )

    @staticmethod
    def inserir_produto():
        nome = request.form.get("produto")
        preco = request.form.get("preco")

        # Tratamento simples
        if not nome or not preco:
            return "Nome e preço são obrigatórios!", 400

        try:
            preco = float(preco)
        except:
            return "Preço inválido!", 400

        ProdutoModel.inserir(nome, preco)

        # Após inserir, volta para a página 1 da paginação
        return render_template(
            "sucesso.html",
            mensagem="Produto inserido com sucesso!"
        )
