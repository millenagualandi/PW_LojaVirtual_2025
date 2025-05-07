from data.produto_model import Produto
from data.produto_sql import CRIAR_TABELA, INSERIR_PRODUTO, OBTER_TODOS
from data.util import get_connection

def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA)
    conn.commit()
    conn.close()

def inserir_produto(produto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(INSERIR_PRODUTO, (produto.nome, produto.descricao, produto.preco, produto.quantidade))
    conn.commit()
    conn.close()

def obter_todos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_TODOS)
    produtos = cursor.fetchall()
    produtos = [Produto(id=row[0], nome=row[1], descricao=row[2], preco=row[3], quantidade=row[4]) for row in produtos]
    conn.close()
    return produtos