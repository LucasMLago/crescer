import streamlit as st
import altair as alt
import pandas as pd
import altair_charts
import plotly.express as px
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

map_perguntas = {
    "1. Distribuição por ano das matérias sobre suicídio com o público infanto-juvenil": {
        'csv': get_path('dfs_perguntas','pergunta_1.csv'),
        'chart': altair_charts.chart_1
    },
    "2. Distribuição dos enfoques ao longo dos anos": {
        'csv': get_path('dfs_perguntas','pergunta_2.csv'),
        'chart': altair_charts.chart_2
    },
    "3. Fontes das reportagens": {
        'csv': get_path('dfs_perguntas','pergunta_3.csv'),
        'chart': altair_charts.chart_3
    },
    "4. Distribuição dos riscos ao longo dos anos": {
        'csv': get_path('dfs_perguntas','pergunta_4.csv'),
        'chart': altair_charts.chart_4
    },
    "5. Origem do veículo": {
        'csv': get_path('dfs_perguntas','pergunta_5.csv'),
        'chart': altair_charts.chart_5
    },
    "6. Recomendações de ações/agentes/entes para solucionar a ideação suicida": {
        'csv': get_path('dfs_perguntas','pergunta_6.csv'),
        'chart': altair_charts.chart_6
    },
    "7. A quem se destina a reportagem": {
        'csv': get_path('dfs_perguntas','pergunta_7.csv'),
        'chart': altair_charts.chart_7
    },
    "8. Riscos envolvidos no suicídio": {
        'csv': get_path('dfs_perguntas','pergunta_8.csv'),
        'chart': altair_charts.chart_8
    },
    "9. Especulações sobre causa(s) do suicídio": {
        'csv': get_path('dfs_perguntas','pergunta_9.csv'),
        'chart': altair_charts.chart_9
    },
    "10. Prioridade da reportagem/coluna": {
        'csv': get_path('dfs_perguntas','pergunta_10.csv'),
        'chart': altair_charts.chart_10
    },
    "11. Imagens que ilustram a reportagem": {
        'csv': get_path('dfs_perguntas','pergunta_11.csv'),
        'chart': altair_charts.chart_11
    },
    "12. Distribuição das especulações das causas de suicidio ao longo dos anos": {
        'csv': get_path('dfs_perguntas','pergunta_12.csv'),
        'chart': altair_charts.chart_12
    }
}

with st.container(height=None, border=True):
    perguntas = list(map_perguntas.keys())
    
    st.header('Selecione uma Análise da :blue[Revista Crescer] 🔎')
    select = st.selectbox('Selecione uma Análise da Revista Crescer', options=perguntas, index=None, placeholder='Escolha uma opção', label_visibility='collapsed')
    
    if select in map_perguntas:
        config = map_perguntas[select]
        df = pd.read_csv(config['csv'])
        
        st.dataframe(
            data=df,
            column_config={
                "ANO": st.column_config.NumberColumn(format="%d")} if "ANO" else None,
            use_container_width=True,
            hide_index=True
        )
        st.markdown('---')
        if select.startswith('2') or select.startswith('4') or select.startswith('12'):
            st.plotly_chart(config['chart'], use_container_width=True)
        else:
            st.altair_chart(config['chart'], use_container_width=True)
