import pandas as pd
import sqlite3


# Criando o objeto Conn 
conn = sqlite3.connect('tcc.db')
c = conn.cursor() #"C nosso cursor, a partir dele que executamos todas nossas ações, criação de tabelas etc"

# 
c.execute("""CREATE TABLE IF NOT EXISTS processos (
            'No Processo' number,
            Empresa text,
            Tipo text,
            Ação text,
            Vara text,
            Fase text,
            Instância number,
            'Data Inicial' text,
            'Data Final' text,
            'Processo Concluído' number,
            'Processo Vencido' number,
            Advogados text,
            Cliente text,
            'Cpf Cliente' number,
            'Descrição' text)""")

c.execute("""CREATE TABLE IF NOT EXISTS advogados (
            Advogado text,
            OAB number,
            CPF number)""")

df_adv = pd.read_sql("SELECT * FROM advogados", conn)
df_proc = pd.read_sql("SELECT * FROM processos", conn)

conn.commit()
conn.close()