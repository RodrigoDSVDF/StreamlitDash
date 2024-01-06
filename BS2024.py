import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st

def main():
    st.title('Histórico de Preços de Fechamento para Empresas B3')

    tabela = pd.read_csv(r"C:\Users\Rodrigo_df\empresas_b3.csv")
    st.dataframe(tabela)

    for empresa in tabela['Sigla']:
        st.write(empresa)

        try:
            cotacao = yf.download(f'{empresa}.SA', start='2023-01-01', end='2024-01-05')
            st.dataframe(cotacao)

            fig, ax = plt.subplots(figsize=(14, 7))
            ax.plot(cotacao['Close'])
            ax.set_title(f'Histórico de Preços de Fechamento para {empresa}')
            ax.set_xlabel('Data')
            ax.set_ylabel('Preço de Fechamento')
            ax.grid(True)

            st.pyplot(fig)

        except Exception as e:
            st.write(f"Erro ao obter dados para {empresa}: {e}")

if __name__ == "__main__":
    main()

