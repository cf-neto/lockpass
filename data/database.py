import sqlite3 as sql
import os

# Caminho para o banco de dados (mesma pasta do database.py)
DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

def conectar():
    return sql.connect(DB_PATH)

def criar_tabela():
    CON = conectar()
    CUR = CON.cursor()
    CUR.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            app TEXT NOT NULL,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    """)
    CON.commit()
    CON.close()

def inserir(app, nome, senha):
    CON = conectar()
    CUR = CON.cursor()
    CUR.execute("INSERT INTO data (app, nome, senha) VALUES (?, ?, ?)", (app, nome, senha))
    CON.commit()
    CON.close()

def listar():
    CON = conectar()
    CUR = CON.cursor()
    CUR.execute("SELECT app, nome, senha FROM data")
    dados = CUR.fetchall()
    CON.close()
    return dados

def remover(app):
    CON = conectar()
    CUR = CON.cursor()
    CUR.execute("DELETE FROM data WHERE app = ?", (app,))
    CON.commit()
    CON.close()
