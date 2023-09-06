import pandas as pd
import streamlit as st
import joblib

# Carregue o modelo de previsão de empréstimos treinado
modelo = joblib.load('C:\\Users\\wggso\\OneDrive\\Documentos\\Data_Science\\Predict Loan Eligibility for Dream Housing Finance company\\modelo_emprestimos.joblib')


# Crie um dicionário com os nomes das colunas do conjunto de dados
colunas = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
           'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
           'Loan_Amount_Term', 'Credit_History', 'Property_Area_Rural',
           'Property_Area_Semiurban', 'Property_Area_Urban']  # Adicione as características faltantes aqui

# Crie um dicionário para armazenar os valores inseridos pelo usuário
entrada_usuario = {}

# Solicite os valores ao usuário para cada coluna
for coluna in colunas:
    if coluna == 'Credit_History':
        valor = st.selectbox(f'{coluna}', (0.0, 1.0))
    elif coluna == 'Dependents':
        valor = st.selectbox(f'{coluna}', ('0', '1', '2', '3+'))
    else:
        valor = st.text_input(f'{coluna}', '')

    entrada_usuario[coluna] = valor

# Crie um botão para fazer a previsão
botao = st.button('Prever Aprovação de Empréstimo')

if botao:
    # Crie um DataFrame com os valores inseridos pelo usuário
    dados_usuario = pd.DataFrame(entrada_usuario, index=[0])

    # Faça a previsão usando o modelo carregado
    previsao = modelo.predict(dados_usuario)

    # Exiba o resultado da previsão
    if previsao[0] == 'Y':
        st.write('Aprovação de Empréstimo: Sim')
    else:
        st.write('Aprovação de Empréstimo: Não')


# Comandos no terminal, para executar o streal
# 
# cd "c:/Users/wggso/OneDrive/Documentos/Data_Science/Predict Loan Eligibility for Dream Housing Finance company/"
# streamlit run Deploy.py