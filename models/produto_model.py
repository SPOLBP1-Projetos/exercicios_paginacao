from models.db import get_connection

class ProdutoModel:

    @staticmethod
    def listar_todos():
        conn = get_connection()
        cur = conn.cursor()
        res = cur.execute("SELECT * FROM produtos").fetchall()
        conn.close()
        return res

    @staticmethod
    def buscar_por_id(produto_id):
        conn = get_connection()
        cur = conn.cursor()
        res = cur.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,)).fetchone()
        conn.close()
        return res

    @staticmethod
    def buscar_por_nome(nome):
        conn = get_connection()
        cur = conn.cursor()
        res = cur.execute("SELECT * FROM produtos WHERE nome LIKE ?", (f"%{nome}%",)).fetchall()
        conn.close()
        return res

    @staticmethod
    def listar_paginado(offset, limit):
        conn = get_connection()
        cur = conn.cursor()
        res = cur.execute("SELECT * FROM produtos LIMIT ? OFFSET ?", (limit, offset)).fetchall()
        conn.close()
        return res

    @staticmethod
    def contar():
        conn = get_connection()
        cur = conn.cursor()
        total = cur.execute("SELECT COUNT(*) FROM produtos").fetchone()[0]
        conn.close()
        return total
    
    @staticmethod
    def inserir(nome, preco):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", (nome, preco))
        conn.commit()
        conn.close()

    @staticmethod
    def excluir(produto_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
        conn.commit()
        conn.close()
