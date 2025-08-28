# --- 1. Importação de Bibliotecas e Configuração Inicial ---
# Importa as bibliotecas necessárias para a aplicação
import streamlit as st
import pandas as pd
import plotly.express as px
import os
from scipy import stats
import math

# Define o nome do arquivo de dados
DATA_FILE = 'dados-completos-Ituano.csv'

# Configura o layout da página para ser mais amplo
st.set_page_config(layout="wide", page_title="Análise de Dados")

# Aplica CSS personalizado para um tema escuro e visual de cartões
st.markdown("""
<style>
    /* Estilos Gerais da Página */
    .stApp {
        background-color: #0c0e14;
        color: #f1f1f1;
        font-family: 'Inter', sans-serif;
    }
    
    /* Estilos para títulos e subtítulos */
    h1 {
        color: #e5e5e5;
        text-align: center;
        font-weight: 700;
        letter-spacing: 1px;
    }
    
    .css-1av61s0, .st-bh, .st-bb {
        color: #e5e5e5; /* Cor para subtítulos Streamlit */
    }

    /* Estilo para o título de seção dentro dos cards */
    .section-card h2 {
        color: #7ab3ff;
        font-weight: 600;
        margin-bottom: 1.5em;
        text-align: center;
    }

    /* Estilo para a Linha Separadora */
    hr {
        border-top: 1px solid #333;
        margin: 2em 0;
    }
 
    /* Estilo para o texto de métricas */
    .stMetric label {
        font-weight: 600;
    }
    .stMetric p {
        font-size: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Título Principal da Página ---
st.title('Estatísticas do Ituano Futebol Clube')
st.markdown('### Análises estatísticas e visualizações do desempenho do time.')
st.markdown('---')

# --- 2. Carregamento e Processamento de Dados ---
@st.cache_data
def load_data():
    """
    Função para carregar os dados do arquivo CSV e fazer pré-processamento.
    Inclui tratamento de erro caso o arquivo não seja encontrado.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, DATA_FILE)
    
    if not os.path.exists(file_path):
        parent_dir = os.path.dirname(script_dir)
        file_path = os.path.join(parent_dir, DATA_FILE)
        
        if not os.path.exists(file_path):
            st.error(f"Erro: O arquivo '{DATA_FILE}' não foi encontrado.")
            st.info("Por favor, verifique se o arquivo está na pasta 'cp01', a mesma que o script principal (1_home.py).")
            st.stop()
    
    try:
        df = pd.read_csv(file_path)
        
        # Pré-processamento simples de colunas
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        
        if 'player_name' in df.columns:
            df['player_name'] = df['player_name'].astype(str).str.strip()
        
        if 'player_sub' in df.columns:
            df['player_sub'] = df['player_sub'].fillna(False).astype(bool)
        
        # Renomeia colunas se necessário para unificar
        rename_map = {
            'statistics_total_passes': 'statistics_total_passes',
            'statistics_total_shots': 'statistics_total_shots',
            'statistics_accurate_passes': 'statistics_accurate_passes',
            'statistics_goals': 'statistics_goals'
        }
        
        for expected, fallback in rename_map.items():
            if fallback not in df.columns:
                # Se a coluna com o nome original não existir, tenta encontrar com um nome alternativo
                if f"_{fallback}" in df.columns:
                    df.rename(columns={f"_{fallback}": expected}, inplace=True)

        return df
    except Exception as e:
        st.error(f"Erro ao ler o arquivo CSV. Detalhes: {e}")
        st.stop()

# Carregar os dados
df = load_data()

# --- 3. Filtros de Dados ---
st.sidebar.title('Filtros de Dados')
st.sidebar.markdown('---')

# Filtro 1: Torneio
if 'tournament' in df.columns:
    tournaments = ['Todos'] + sorted(df['tournament'].dropna().unique().tolist())
    st.sidebar.subheader('Torneio')
    filter_tournament = st.sidebar.selectbox('Selecione o Torneio', tournaments)
else:
    st.sidebar.warning("Coluna 'tournament' não encontrada.")
    filter_tournament = 'Todos'

# Filtro 2: Tipo de jogo (Casa ou Fora)
if 'home_or_away' in df.columns:
    home_away = ['Todos'] + sorted(df['home_or_away'].dropna().unique().tolist())
    st.sidebar.subheader('Local do Jogo')
    filter_home_away = st.sidebar.selectbox('Onde foi o Jogo?', home_away)
else:
    st.sidebar.warning("Coluna 'home_or_away' não encontrada.")
    filter_home_away = 'Todos'

# Aplica os filtros
df_filtered = df.copy()

if filter_tournament != 'Todos':
    df_filtered = df_filtered[df_filtered['tournament'] == filter_tournament]

if filter_home_away != 'Todos':
    df_filtered = df_filtered[df_filtered['home_or_away'] == filter_home_away]

# --- 4. Tabela de Jogos e Resumo das Perguntas ---
st.markdown(f'<div class="section-card">', unsafe_allow_html=True)
st.markdown(f'<h2>Tabela de Jogos</h2>', unsafe_allow_html=True)
st.markdown('Esta tabela exibe os dados dos jogos, permitindo uma visão geral das informações disponíveis.')
df_table = df_filtered.drop(columns=[col for col in df_filtered.columns if df_filtered[col].isnull().all()])
st.dataframe(df_table, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('---')

st.markdown('### Perguntas a serem respondidas na análise:')
st.markdown("""
- **Pergunta 1:** Qual a classificação das variáveis no conjunto de dados?
- **Pergunta 2:** Quais jogadores marcaram mais gols e qual o total de gols encontrados?
- **Pergunta 3:** Qual é a distribuição de uma variável numérica, como o total de passes, e como se comparam suas medidas de tendência central?
- **Pergunta 4:** Qual é a estimativa mais provável para a média do número de chutes ao gol de um jogador?
- **Pergunta 5:** A média de passes precisos do time é estatisticamente diferente de um valor específico?
""")
st.markdown('---')

# --- Seção 1: Pergunta 1 ---
st.markdown(f'<div class="section-card">', unsafe_allow_html=True)
st.markdown('<h2>Seção 1: Análise das Variáveis</h2>', unsafe_allow_html=True)
st.markdown('### Pergunta 1: Qual a classificação das variáveis no conjunto de dados?')
st.markdown('---')
col_tool, col_resp = st.columns([3, 1])

with col_tool:
    st.subheader('Tabela de Classificação de Dados')
    data = {
        'Variável': [
            '`team_name`', '`home_or_away`', '`tournament`', '`player_name`', '`player_position`',
            '`statistics_goals`', '`statistics_assists`', '`statistics_total_passes`', '`statistics_accurate_shots`', '`player_number`'
        ],
        'Tipo de dado': [
            'Qualitativa (Nominal)', 'Qualitativa (Nominal)', 'Qualitativa (Nominal)', 'Qualitativa (Nominal)', 'Qualitativa (Nominal)',
            'Quantitativa (Discreta)', 'Quantitativa (Discreta)', 'Quantitativa (Discreta)', 'Quantitativa (Discreta)', 'Quantitativa (Discreta)'
        ],
        'Explicação': [
            'Categoria para o nome do time.', 'Categoria para o local do jogo.', 'Categoria para o nome do torneio.', 'Categoria para o nome do jogador.', 'Categoria para a posição do jogador.',
            'Número de gols (contagem).', 'Número de assistências (contagem).', 'Número total de passes (contagem).', 'Número de chutes precisos (contagem).', 'Número da camisa (identificador numérico).'
        ]
    }
    df_types = pd.DataFrame(data)
    st.dataframe(df_types, use_container_width=True)
    st.markdown("""
    Esta tabela detalha cada variável do conjunto de dados, classificando-a como **Qualitativa** (descrições) ou **Quantitativa** (números). É o ponto de partida para qualquer análise.
    """)

with col_resp:
    st.markdown('<div class="text-card">', unsafe_allow_html=True)
    st.subheader('Resposta da Pergunta 1')
    st.success("""
    O conjunto de dados apresenta uma composição diversificada, combinando variáveis **qualitativas** e **quantitativas**. As variáveis qualitativas, como o `tournament` e a `player_position`, são essenciais para categorizar os dados, enquanto as variáveis quantitativas, como o `statistics_goals` e os `statistics_total_passes`, fornecem os valores numéricos para as análises estatísticas mais aprofundadas. Esta diversidade permite que a análise explore tanto as características descritivas quanto o desempenho numérico do time e dos jogadores.
    """)
    st.subheader('Explicação da Resposta')
    st.markdown("""
    A distinção entre esses tipos de dados é o primeiro e mais crucial passo para uma análise estatística. As variáveis qualitativas (`team_name`, `tournament`) permitem agrupar e categorizar os dados, enquanto as variáveis quantitativas (`statistics_goals`, `statistics_total_passes`) possibilitam a realização de cálculos e testes estatísticos, como médias, desvios e regressões.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('---')

# --- Seção 2: Pergunta 2 ---
st.markdown(f'<div class="section-card">', unsafe_allow_html=True)
st.markdown('<h2>Seção 2: Análise de Gols</h2>', unsafe_allow_html=True)
st.markdown('### Pergunta 2: Quais jogadores marcaram mais gols e qual o total de gols encontrados?')
st.markdown('---')
col_tool, col_resp = st.columns([3, 1])

with col_tool:
    st.subheader('Gráfico de Gols por Jogador')
    if 'statistics_goals' in df_filtered.columns and pd.api.types.is_numeric_dtype(df_filtered['statistics_goals']):
        goals_df = df_filtered[df_filtered['statistics_goals'] > 0]
        
        if not goals_df.empty:
            goals_by_player = goals_df.groupby('player_name')['statistics_goals'].sum().reset_index()
            goals_by_player = goals_by_player.sort_values(by='statistics_goals', ascending=False)
            
            total_goals = goals_by_player['statistics_goals'].sum()
            st.info(f"Total de gols encontrados: **{total_goals:,.0f}**")
            
            fig_goals = px.bar(goals_by_player, x='player_name', y='statistics_goals',
                             title="Gols Marcados por Jogador",
                             labels={'player_name': 'Jogador', 'statistics_goals': 'Total de Gols'},
                             color_discrete_sequence=px.colors.qualitative.Plotly)
            st.plotly_chart(fig_goals, use_container_width=True)
        else:
            st.info("Nenhum gol encontrado com os filtros selecionados.")
    else:
        st.info("A coluna 'statistics_goals' não foi encontrada ou não é numérica.")

with col_resp:
    st.markdown('<div class="text-card">', unsafe_allow_html=True)
    st.subheader('Resposta da Pergunta 2')
    if 'statistics_goals' in df_filtered.columns and pd.api.types.is_numeric_dtype(df_filtered['statistics_goals']):
        goals_df = df_filtered[df_filtered['statistics_goals'] > 0]
        if not goals_df.empty:
            goals_by_player = goals_df.groupby('player_name')['statistics_goals'].sum().reset_index()
            goals_by_player = goals_by_player.sort_values(by='statistics_goals', ascending=False)
            total_goals = goals_by_player['statistics_goals'].sum()
            top_scorer = goals_by_player.iloc[0]['player_name']
            top_scorer_goals = goals_by_player.iloc[0]['statistics_goals']
            st.success(f"""
            O total de gols encontrados no conjunto de dados é de **{total_goals:,.0f}**. Deste total, o artilheiro do time é o jogador **{top_scorer}**, que contribuiu com uma parte significativa, marcando **{top_scorer_goals:,.0f}** gols. A análise do gráfico de barras mostra a distribuição de gols entre todos os jogadores, destacando a importância de {top_scorer} para o desempenho ofensivo da equipe.
            """)
        else:
            st.warning("""
            Nenhum gol foi encontrado com os filtros selecionados, impossibilitando a análise.
            """)
    else:
        st.error("""
        A coluna `statistics_goals` não foi encontrada no conjunto de dados.
        """)
    st.subheader('Análise do Gráfico')
    st.markdown("""
    O gráfico de barras visualiza a quantidade total de gols marcados por cada jogador, permitindo que você identifique rapidamente os artilheiros do time. A altura de cada barra corresponde ao número de gols, e a interação com o mouse revela informações detalhadas.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('---')

# --- Seção 3: Pergunta 3 ---
st.markdown(f'<div class="section-card">', unsafe_allow_html=True)
st.markdown(f'<h2>Seção 3: Análise de Distribuição</h2>', unsafe_allow_html=True)
st.markdown('### Pergunta 3: Qual é a distribuição de uma variável numérica, como o total de passes, e como se comparam suas medidas de tendência central?')
st.markdown('---')
col_graph_stats, col_text_stats = st.columns([3, 1])

with col_graph_stats:
    st.subheader('Distribuição de Dados com Medidas Estatísticas')
    
    numeric_cols = df_filtered.select_dtypes(include=['number']).columns.tolist()
    if 'statistics_total_passes' in numeric_cols:
        selected_col = 'statistics_total_passes'
    elif numeric_cols:
        selected_col = st.selectbox('Selecione uma coluna para análise', numeric_cols, key='dist_analysis_select')
    else:
        st.warning("Não há colunas numéricas no seu arquivo para realizar a análise.")
        st.stop()
        
    data_to_analyze = df_filtered[selected_col].dropna()

    if not data_to_analyze.empty:
        fig = px.histogram(data_to_analyze, x=selected_col, nbins=20, 
                           title=f'Histograma da coluna {selected_col}', 
                           template='plotly_dark')
        
        mean_val = data_to_analyze.mean()
        fig.add_vline(x=mean_val, line_width=4, line_dash="dash", line_color="red", 
                      annotation_text=f"Média: {mean_val:,.2f}", annotation_position="top right", 
                      annotation_font_color="red")
        
        median_val = data_to_analyze.median()
        fig.add_vline(x=median_val, line_width=4, line_dash="dash", line_color="green", 
                      annotation_text=f"Mediana: {median_val:,.2f}", annotation_position="top left",
                      annotation_font_color="green")
        
        mode_result = data_to_analyze.mode()
        if not mode_result.empty and len(mode_result) == 1:
            mode_val = mode_result[0] 
            fig.add_vline(x=mode_val, line_width=4, line_dash="dash", line_color="yellow", 
                          annotation_text=f"Moda: {mode_val:,.2f}", annotation_position="bottom right",
                          annotation_font_color="yellow")
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Não há dados suficientes para criar o gráfico com os filtros selecionados.") 

with col_text_stats:
    st.markdown('<div class="text-card">', unsafe_allow_html=True)
    st.subheader('Resposta da Pergunta 3')
    if not data_to_analyze.empty:
        mean_val = data_to_analyze.mean()
        median_val = data_to_analyze.median()
        mode_result = data_to_analyze.mode()
        
        st.success(f"""
        A distribuição dos dados para a variável **`{selected_col}`** é concentrada em torno das medidas de tendência central, que são notavelmente próximas umas das outras. A **Média** (`{mean_val:,.2f}`), a **Mediana** (`{median_val:,.2f}`) e a **Moda** (`{mode_result[0]:,.2f}` se houver) se alinham de perto, indicando que a distribuição é bastante simétrica, com pouca influência de valores extremos. Isso sugere que a maioria dos jogadores ou eventos está consistentemente dentro de um desempenho esperado para esta variável.
        """)
    else:
        st.warning("Não há dados para analisar a distribuição. Por favor, ajuste os filtros.")

    st.subheader('Explicação da Resposta') 
    st.markdown("""
    * **Média (linha vermelha):** É o valor central, ou a média aritmética dos dados. É sensível a valores extremos. 
    * **Mediana (linha verde):** É o valor que divide a amostra exatamente ao meio. 50% dos dados estão abaixo dele e 50% estão acima. É menos sensível a valores extremos. 
    * **Moda (linha amarela):** É o valor que aparece com mais frequência. 
    
    A proximidade desses valores no histograma indica que a distribuição não tem grandes picos ou dispersões extremas, o que a torna um bom resumo para o conjunto de dados.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('---')

 # --- Seção 4: Pergunta 4 --- 
st.markdown(f'<div class="section-card">', unsafe_allow_html=True)
st.markdown(f'<h2>Seção 4: Análise de Intervalo de Confiança</h2>', unsafe_allow_html=True)
st.markdown('### Pergunta 4: Qual é a estimativa mais provável para a média do número de chutes ao gol de um jogador?')
st.markdown('---')
col_ic_tool, col_ic_resp = st.columns([3, 1])

with col_ic_tool:
    st.subheader('Intervalo de Confiança') 

    numeric_cols_ic = df_filtered.select_dtypes(include=['number']).columns.tolist()
    if 'statistics_total_shots' in numeric_cols_ic:
        selected_col_ic = 'statistics_total_shots'
    elif numeric_cols_ic:
        selected_col_ic = st.selectbox('Selecione uma coluna para análise de IC', numeric_cols_ic, key='ic_select')
    else:
        st.warning("Não há colunas numéricas para realizar a análise de Intervalo de Confiança.") 
        st.stop()
        
    data_to_analyze_ic = df_filtered[selected_col_ic].dropna()

    if len(data_to_analyze_ic) > 1:
        st.markdown('**Configurações do Intervalo de Confiança**') 
        confidence_level = st.slider(
            'Selecione o Nível de Confiança (%)', 
            min_value=80,
            max_value=99,
            value=95,
            step=1,
            key='ic_slider'
        ) / 100.0

        mean_ic = data_to_analyze_ic.mean()
        n_ic = len(data_to_analyze_ic)
        std_err_ic = stats.sem(data_to_analyze_ic)
        
        interval = stats.t.interval(confidence_level, n_ic - 1, loc=mean_ic, scale=std_err_ic)

        st.markdown(f"**Média da amostra:** `{mean_ic:,.2f}`") 
        st.metric(
            label=f"Intervalo de Confiança ({confidence_level*100:.0f}%)", 
            value=f"De {interval[0]:,.2f} a {interval[1]:,.2f}"
        )
    else:
        st.info("Não há dados suficientes para calcular o intervalo de confiança com os filtros selecionados.") 

with col_ic_resp:
    st.markdown('<div class="text-card">', unsafe_allow_html=True)
    st.subheader('Resposta da Pergunta 4') 
    if len(data_to_analyze_ic) > 1:
        st.success(f"""
        Com base na amostra de dados e no nível de confiança de **{confidence_level*100:.0f}%** que você selecionou, a média real do número de chutes a gol por jogador na população completa de dados tem uma alta probabilidade de estar entre **{interval[0]:,.2f}** e **{interval[1]:,.2f}**. Este intervalo representa a estimativa mais confiável para o desempenho médio de chutes a gol do time.
        """)
    else:
        st.warning("Não há dados suficientes para calcular o intervalo de confiança.")

    st.subheader('O que é o Intervalo de Confiança?') 
    st.markdown("""
    O **Intervalo de Confiança (IC)** é uma faixa de valores que provavelmente contém o verdadeiro valor da média da população. 
    
    * **Nível de Confiança:** Representa a chance de que o IC realmente contenha a média real. Um nível de 95% significa que, se você repetir a pesquisa 100 vezes, o IC calculado em 95 delas conterá a média verdadeira. 
    
    * **Interpretação:** Um intervalo mais estreito indica uma estimativa mais precisa. Um intervalo mais largo indica mais incerteza nos dados.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('---')

# --- Seção 5: Pergunta 5 --- 
st.markdown(f'<div class="section-card">', unsafe_allow_html=True)
st.markdown(f'<h2>Seção 5: Testes de Hipótese</h2>', unsafe_allow_html=True)
st.markdown('### Pergunta 5: A média de passes precisos do time é estatisticamente diferente de um valor específico?')
st.markdown('---')
col_test_graph, col_test_text = st.columns([3, 1])

with col_test_graph:
    st.subheader('Teste t de uma Amostra') 
    
    test_cols = df_filtered.select_dtypes(include=['number']).columns.tolist()
    if 'year' in test_cols:
        test_cols.remove('year')

    if not test_cols:
        st.warning("Não há colunas numéricas adequadas para realizar testes de hipótese.") 
        st.stop()
        
    if 'statistics_accurate_passes' in test_cols:
        selected_test_col = 'statistics_accurate_passes'
    else:
        selected_test_col = st.selectbox('Selecione a coluna para o teste', test_cols, key='test_select')
    
    col_test_select, col_test_value = st.columns(2)
    with col_test_select:
        st.markdown(f'**Coluna Selecionada:** `{selected_test_col}`')
    with col_test_value:
        hypothesized_value = st.number_input(
            'Insira o valor hipotético da média da população',
            value=float(df_filtered[selected_test_col].mean()),
            key='hyp_value'
        )

    st.markdown('**Configuração do Teste**')
    alternative_options = {
        'Duas faces': 'two-sided',
        'Maior que': 'greater',
        'Menor que': 'less'
    }
    selected_alternative_label = st.selectbox(
        'Selecione o tipo de teste',
        list(alternative_options.keys()),
        key='alternative_selection'
    )
    alternative = alternative_options[selected_alternative_label]

    data_for_test = df_filtered[selected_test_col].dropna()

    if len(data_for_test) > 1:
        t_statistic, p_value = stats.ttest_1samp(data_for_test, popmean=hypothesized_value, alternative=alternative)

        st.subheader('Resultados do Teste t')
        col_t_stat, col_p_value = st.columns(2)
        with col_t_stat:
            st.metric(label="Estatística T", value=f"{t_statistic:,.4f}")
        with col_p_value:
            st.metric(label="Valor-P", value=f"{p_value:,.4f}")

        st.subheader('Visualização do Teste')
        fig_test = px.histogram(data_for_test, x=selected_test_col, nbins=20,
                                 title=f'Distribuição de {selected_test_col}', 
                                 template='plotly_dark')
        fig_test.add_vline(x=data_for_test.mean(), line_dash="dash", line_color="blue",
                           annotation_text=f"Média da Amostra: {data_for_test.mean():,.2f}",
                           annotation_position="top left")
        fig_test.add_vline(x=hypothesized_value, line_dash="dash", line_color="red",
                           annotation_text=f"Valor Hipotético: {hypothesized_value:,.2f}",
                           annotation_position="top right")
        st.plotly_chart(fig_test, use_container_width=True)

    else:
        st.info("Dados insuficientes para realizar o teste de hipótese. Por favor, ajuste os filtros ou selecione outra coluna.")

with col_test_text:
    st.markdown('<div class="text-card">', unsafe_allow_html=True)
    st.subheader('Resposta da Pergunta 5')
    if len(data_for_test) > 1:
        # CORREÇÃO AQUI: Verificando o valor-p corretamente
        if p_value < 0.05:
            st.success(f"O P-valor de `{p_value:,.4f}` é menor que o nível de significância de 0.05. Isso significa que a diferença entre a média de passes da amostra e o valor hipotético de `{hypothesized_value:,.2f}` **é estatisticamente significativa**. Portanto, temos evidências para rejeitar a hipótese nula e concluir que a média real da população é, de fato, diferente do valor hipotético.")
        else:
            st.warning(f"O P-valor de `{p_value:,.4f}` é maior ou igual ao nível de significância de 0.05. Não há evidências estatísticas suficientes para afirmar que a média de passes do time é diferente do valor hipotético de `{hypothesized_value:,.2f}`. Neste caso, não podemos rejeitar a hipótese nula.")
    else:
        st.warning("Não foi possível realizar o teste devido à falta de dados.")

    st.subheader('Explicação do Teste t')
    st.markdown("""
    Este teste compara a **média da sua amostra** com um **valor hipotético** que você definiu.
    
    * **Hipótese Nula ($H_0$):** A média da amostra é igual ao valor hipotético.
    * **Hipótese Alternativa ($H_a$):** A média da amostra é diferente (ou maior/menor) do valor hipotético.
    
    * **T-Statistic:** Uma medida de quão distante a média da sua amostra está do valor hipotético.
    * **P-valor:** A probabilidade de você obter a sua amostra (ou uma mais extrema) se a hipótese nula for verdadeira.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('---')
