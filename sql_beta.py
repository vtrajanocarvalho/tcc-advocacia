import pandas as pd
import sqlite3


# Criando o objeto Conn 
conn = sqlite3.connect('tcc.db')
c = conn.cursor() #"C nosso cursor, a partir dele que executamos todas nossas ações, criação de tabelas etc"

# 
c.execute("""CREATE TABLE IF NOT EXISTS processos (
            'Processo' Int,
            Empresa text,
            Tipo text,
            Ação text,
            Vara text,
            Fase text,
            Instância Int,
            'Data Inicial' Date,
            'Data Final' Date,
            'Processo Concluído' Int,
            'Processo Vencido' Int,
            Advogados text,
            Cliente text,
            'Cpf Cliente' Int,
            'Descrição' text)""")

c.execute("""CREATE TABLE IF NOT EXISTS advogados (
            Advogado text,
            OAB Int,
            CPF Int)""")

df_adv = pd.read_sql("SELECT * FROM advogados", conn)
df_proc = pd.read_sql("SELECT * FROM processos", conn)

conn.commit()
conn.close()