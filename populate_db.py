from models.db import get_connection

PRODUTOS = [
    ("Notebook Gamer X", 5200),
    ("Mouse sem Fio", 150),
    ("Teclado Mecânico RGB", 350),
    ("Monitor 27 polegadas", 150),
    ("SSD 512GB", 10),
    ("Headphones RGB Led", 450),
    ("Teclado Mecânico sem fio", 250),
    ("Gabinete com led", 130),
    ("Alexa oitava geração", 130),
    ("Fones de Ouvido Sem Fio Gamer", 30),
    ("Carregador Turbo 50w", 50),
    ("Mouse Recarregável", 80),
]

conn = get_connection()
cur = conn.cursor()

cur.executemany("INSERT INTO produtos (nome, preco) VALUES (?, ?)", PRODUTOS)

conn.commit()
conn.close()

print("Banco populado!")
