import pandas as pd
import altair as alt
import plotly.express as px
import os

##################### Dataframes #####################

script_dir = os.path.dirname(os.path.abspath(__file__))
dfs_perguntas_dir = os.path.join(script_dir, 'dfs_perguntas')

def get_csv_path(filename):
    return os.path.join(dfs_perguntas_dir, filename)

pergunta_1 = pd.read_csv(get_csv_path('pergunta_1.csv'))
pergunta_2 = pd.read_csv(get_csv_path('pergunta_2.csv'))
pergunta_3 = pd.read_csv(get_csv_path('pergunta_3.csv'))
pergunta_4 = pd.read_csv(get_csv_path('pergunta_4.csv'))
pergunta_5 = pd.read_csv(get_csv_path('pergunta_5.csv'))
pergunta_6 = pd.read_csv(get_csv_path('pergunta_6.csv'))
pergunta_7 = pd.read_csv(get_csv_path('pergunta_7.csv'))
pergunta_8 = pd.read_csv(get_csv_path('pergunta_8.csv'))
pergunta_9 = pd.read_csv(get_csv_path('pergunta_9.csv'))
pergunta_10 = pd.read_csv(get_csv_path('pergunta_10.csv'))
pergunta_11 = pd.read_csv(get_csv_path('pergunta_11.csv'))
pergunta_12 = pd.read_csv(get_csv_path('pergunta_12.csv'))


##################### Gráficos #####################

# GRÁFICO 1
selection = alt.selection_point(fields=['ANO'], empty=True)

chart = alt.Chart(pergunta_1).mark_bar(size=40).encode(
    x=alt.X('ANO:N', title='Ano', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('TOTAL DE MATÉRIAS:Q', title='Total de Matérias', axis=alt.Axis(grid=True), scale=alt.Scale(domain=[0, 26])),
    tooltip=['ANO:N', 'TOTAL DE MATÉRIAS:Q'],
    color=alt.Color(
        'TOTAL DE MATÉRIAS:Q',
        scale=alt.Scale(scheme='blues')
    ),
    opacity=alt.condition(
        selection,
        alt.value(1),
        alt.value(0.3)
    )
).properties(
    title='Total de Matérias por Ano',
    width=800,
    height=400
).add_params(
    selection
)

text = chart.mark_text(
    align='center',
    baseline='middle',
    dy=-10
).encode(
    text=alt.Text('TOTAL DE MATÉRIAS:Q', format=',.0f')
)

chart_1 = chart + text

# GRÁFICO 2
chart_2 = px.bar(
    pergunta_2,
    title='<b>Distribuição dos enfoques por ano</b>',
    x='ANO', 
    y=['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7'],
    labels={'value': 'Quantidade', 'variable': 'Enfoque'},
    height=600
)

# GRÁFICO 3
selection = alt.selection_point(fields=['FONTE'], empty=True)

chart = alt.Chart(pergunta_3).mark_bar().encode(
    x=alt.X('FONTE:N', sort='x', title='Fonte', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('QUANTIDADE:Q', title='Quantidade', scale=alt.Scale(domain=[0, 65])),
    tooltip=['FONTE:N', 'QUANTIDADE:Q'],
    color=alt.condition(
        selection,
        alt.Color('FONTE:N'),
        alt.value('lightgray')
    ),
    opacity=alt.condition(
        selection,
        alt.value(1),
        alt.value(0.3)
    )
).properties(
    title='Fonte da reportagem',
    width=800,
    height=400
).add_params(
    selection
)

text = chart.mark_text(
    align='center',
    baseline='bottom',
    dy=-5,
    fontWeight='bold'
).encode(
    text=alt.Text('QUANTIDADE:Q')
)

chart_3 = chart + text

# GRÁFICO 4
chart_4 = px.bar(
    pergunta_4,
    title='<b>Distribuição dos Riscos ao Longo dos Anos</b>',
    x='ANO',
    y='QUANTIDADE',
    color='RISCOS',
    labels={'ANO': 'Ano', 'QUANTIDADE': 'Quantidade', 'RISCOS': 'Riscos'},
    template='plotly_white'
)

chart_4.update_layout(
    xaxis_title='Ano',
    yaxis_title='Quantidade',
    barmode='stack',
    height=600
)

# GRÁFICO 5
selection = alt.selection_point(fields=['ORIGEM'], empty=True)

chart = alt.Chart(pergunta_5).mark_bar().encode(
    x=alt.X('ORIGEM:N', title='Origem', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('QUANTIDADE:Q', title='Quantidade'),
    tooltip=['ORIGEM:N', 'QUANTIDADE:Q'],
    color=alt.condition(
        selection,
        alt.Color('ORIGEM:N', title='Origem'),
        alt.value('lightgrey')
    ),
    opacity=alt.condition(
        selection,
        alt.value(1),
        alt.value(0.3)
    )
).properties(
    title='Origem do veículo',
    width=800,
    height=400
).add_params(
    selection
)

text = chart.mark_text(
    align='center',
    baseline='bottom',
    dy=-5,
    fontWeight='bold'
).encode(
    text=alt.Text('QUANTIDADE:Q')
)

chart_5 = chart + text

# GRÁFICO 6
selection = alt.selection_point(fields=['SOLUÇÃO'], empty=True)

chart = alt.Chart(pergunta_6).mark_bar().encode(
    x=alt.X('SOLUÇÃO:N', sort='x', title='Solução', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('count():Q', title='Número de Ocorrências'),
    tooltip=['SOLUÇÃO:N', alt.Tooltip('count():Q', title='QUANTIDADE')],
    color=alt.condition(
        selection,
        alt.Color('SOLUÇÃO:N'),
        alt.value('lightgrey')
    ),
    opacity=alt.condition(
        selection,
        alt.value(1),
        alt.value(0.3)
    )
).properties(
    title='Recomendações de ações/agentes/entes para solucionar a ideação suicida',
    width=800,
    height=400
).add_params(
    selection
)

text = chart.mark_text(
    align='center',
    baseline='bottom',
    dy=-5,
    fontWeight='bold'
).encode(
    text=alt.Text('count():Q')
)

chart_6 = chart + text

# GRÁFICO 7
selection = alt.selection_point(fields=['ENFOQUE'], empty=True)

chart = alt.Chart(pergunta_7).mark_bar().encode(
    x=alt.X('ENFOQUE:N', sort='x', title='Enfoque', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('QUANTIDADE:Q', title='Número de Enfoques', scale=alt.Scale(domain=[0, 70])),
    tooltip=['ENFOQUE:N', 'QUANTIDADE:Q'],
    color=alt.condition(
        selection,
        alt.Color('ENFOQUE:N'),
        alt.value('lightgray')
    ),
    opacity=alt.condition(
        selection,
        alt.value(1),
        alt.value(0.3)
    )
).properties(
    title='A quem se destina a reportagem',
    width=800,
    height=400
).add_params(
    selection
)

text = chart.mark_text(
    align='center',
    baseline='bottom',
    dy=-5,
    fontWeight='bold'
).encode(
    text=alt.Text('QUANTIDADE:Q')
)

chart_7 = chart + text

# GRÁFICO 8
selection = alt.selection_point(fields=['RISCO'], empty=True)

chart = alt.Chart(pergunta_8).mark_bar().encode(
    x=alt.X('RISCO:N', sort='-y', title='Risco', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('QUANTIDADE:Q', title='Número de Ocorrências'),
    tooltip=['RISCO:N', 'QUANTIDADE:Q'],
    color=alt.condition(
        selection,
        alt.Color('RISCO:N'),
        alt.value('lightgray')
    ),
    opacity=alt.condition(
        selection,
        alt.value(1),
        alt.value(0.3)
    )
).properties(
    title='Riscos envolvidos no suicídio',
    width=800,
    height=400
).add_params(
    selection
)

text = chart.mark_text(
    align='center',
    baseline='bottom',
    dy=-5,
    fontWeight='bold'
).encode(
    text=alt.Text('QUANTIDADE:Q')
)

chart_8 = chart + text

# GRÁFICO 9
selection = alt.selection_point(fields=['ESPECULAÇÃO'], empty=True)

chart = alt.Chart(pergunta_9).mark_bar().encode(
    x=alt.X('ESPECULAÇÃO:N', sort='-y', title='Especulação', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('QUANTIDADE:Q', title='Número de Reportagens'),
    tooltip=['ESPECULAÇÃO:N', 'QUANTIDADE:Q'],
    color=alt.condition(
        selection,
        alt.Color('ESPECULAÇÃO:N'),
        alt.value('lightgray')
    ),
    opacity=alt.condition(
        selection,
        alt.value(1),
        alt.value(0.3)
    )
).properties(
    title='Especulações sobre causa(s) do suicídio',
    width=800,
    height=400
).add_params(
    selection
)

text = chart.mark_text(
    align='center',
    baseline='bottom',
    dy=-5,
    fontWeight='bold'
).encode(
    text=alt.Text('QUANTIDADE:Q')
)

chart_9 = chart + text

# GRÁFICO 10
selection = alt.selection_point(fields=['PRIORIDADE'], empty=True)

chart = alt.Chart(pergunta_10).mark_bar().encode(
    x=alt.X('PRIORIDADE:N', title='Prioridade', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('QUANTIDADE:Q', title='Quantidade', scale=alt.Scale(domain=[0, 70])),
    tooltip=['PRIORIDADE:N', 'QUANTIDADE:Q'],
    color=alt.condition(
        selection,
        alt.Color('PRIORIDADE:N'),
        alt.value('lightgray')
        ),
    opacity=alt.condition(
        selection,
        alt.value(1),
        alt.value(0.3)
    )
).properties(
    title='Prioridade da reportagem/coluna',
    width=600,
    height=400
).add_params(
    selection
)

text = chart.mark_text(
    align='center',
    baseline='bottom',
    dy=-5,
    fontWeight='bold'
).encode(
    text=alt.Text('QUANTIDADE:Q')
)

chart_10 = chart + text

# GRÁFICO 11
selection = alt.selection_point(fields=['IMAGEM'], empty=True)

chart = alt.Chart(pergunta_11).mark_bar().encode(
    x=alt.X('IMAGEM:N', sort='x', title='Imagem', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('FREQUENCIA:Q', title='Frequência'),
    tooltip=['IMAGEM:N', 'FREQUENCIA:Q'],
    color=alt.condition(
        selection,
        alt.Color('IMAGEM:N'),
        alt.value('lightgray')
    ),
    opacity=alt.condition(
        selection,
        alt.value(1),
        alt.value(0.3)
    )
).properties(
    title='Imagens que ilustram a reportagem',
    width=800,
    height=400
).add_params(
    selection
)

text = chart.mark_text(
    align='center',
    baseline='bottom',
    dy=-5,
    fontWeight='bold'
).encode(
    text=alt.Text('FREQUENCIA:Q')
)

chart_11 = chart + text

# GRÁFICO 12
chart_12 = px.bar(
    pergunta_12,
    title='<b>Distribuição das especulações das causas de suicidio ao longo dos anos</b>',
    x='ANO',
    y='QUANTIDADE',
    color='ESPECULAÇÕES',
    labels={'ANO': 'Ano', 'QUANTIDADE': 'Quantidade', 'ESPECULAÇÕES': 'Especulações'},
    template='plotly_white'
)

chart_12.update_layout(
    xaxis_title='Ano',
    yaxis_title='Quantidade',
    barmode='stack',
    height=600
)
