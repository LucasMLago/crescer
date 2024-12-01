import streamlit as st
import pandas as pd
from utils import get_path

st.set_page_config(
    page_title='Revista Crescer',
    page_icon='📰',
    layout='wide'
)

st.logo(
    image=get_path('images','jornal.png'),
    # link='https://revistacrescer.globo.com',
    icon_image=get_path('images','jornal.png')
)

st.html("""
  <style>
    [alt=Logo] {
      height: 4rem;
    }
  </style>
        """)

descricao = '''
    Esta ferramenta foi construida para permitir uma
    compreensão sobre os dados referentes à :blue[Revista
    Crescer] por meio de tabelas dinâmicas e
    gráficos interativos.
'''
st.sidebar.subheader('Sobre:')
st.sidebar.markdown(descricao)

st.header('Tabela com a legenda de cada termo:')
with st.container(height=None, border=True):
    df = pd.read_csv(get_path('pages','legenda.csv'))
    st.dataframe(df, use_container_width=True, hide_index=True)