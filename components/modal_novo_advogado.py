import dash
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

from app import app

# ========= Layout ========= #
layout = dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle("Adicione Um Advogado")),
            dbc.ModalBody([
                dbc.Row([ #inicia a primeira row
                    dbc.Col([
                        dbc.Label("OAB"),
                        dbc.Input(id="adv_oab", placeholder="Apenas números, referente a OAB...", type="number")
                    ], sm=12, md=6),
                    dbc.Col([
                        dbc.Label("CPF"),
                        dbc.Input(id="adv_cpf", placeholder="Apenas números, CPF...", type="number")
                    ], sm=12, md=6),
                ]), #A primeira Row finaliza nessa linha, com os botão OAB E CPF divido em 2 colunas.
                dbc.Row([ #aqui inciamos a segunda row, com o botão Nome.
                    dbc.Col([
                        dbc.Label("Nome"),
                        dbc.Input(id="adv_nome", placeholder="Nome completo do advogado...", type="text")
                    ]),
                ]),
                html.H5(id='div_erro2') #Essa e nossa DIV de erro, pra informar atraves dos callback, se o advogado foi criado de forma correta. 
            ]),
            dbc.ModalFooter([
                dbc.Button("Cancelar", id="cancel_button_novo_advogado", color="danger"),
                dbc.Button("Salvar", id="save_button_novo_advogado", color="success")
            ])
        ], id="modal_new_lawyer", size="lg", is_open=False)


# ======= Callbacks ======== #
# Callback para adicionar novos advogados
@app.callback(
    Output('store_adv', 'data'),
    Output('div_erro2', 'children'),
    Output('div_erro2', 'style'),
    Input('save_button_novo_advogado', 'n_clicks'),
    State('store_adv', 'data'),
    State('adv_nome', 'value'),
    State('adv_oab', 'value'),
    State('adv_cpf', 'value')
)
def novo_adv(n, dataset, nome, oab, cpf):
    erro = []
    style = {}
    if n:
        if None in [nome, oab, cpf]:
            return dataset, ["Todos dados são obrigatórios para registro!"], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}
        
        df_adv = pd.DataFrame(dataset)

        if oab in df_adv['OAB'].values: #aqui ele checa todos os valores da coluna, se cadastrar e ja tiver na base, ele me retorna com dataset abaixo.
            return dataset, ["Número de OAB ja existe no sistema!"], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}
        elif cpf in df_adv['CPF'].values:
            return dataset, ["Número de CPF ja existe no sistema!"], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}
        elif nome in df_adv['Advogado'].values:
            return dataset, [f"Nome {nome} ja existe no sistema!"], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}
        
        df_adv.loc[df_adv.shape[0]] = [nome, oab, cpf]  # type: ignore
        dataset = df_adv.to_dict()
        return dataset, ["Cadastro realizado com sucesso!"], {'margin-bottom': '15px', 'color': 'green', 'text-shadow': '2px 2px 8px #000000'}
    return dataset, erro, style
