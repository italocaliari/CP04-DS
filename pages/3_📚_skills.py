# Importa a biblioteca Streamlit para criar a aplicação web
import streamlit as st

# --- Configurações da Página e Tema Personalizado ---

# Configura o layout da página para ser mais amplo
st.set_page_config(layout="wide", page_title="Habilidades")

# Aplica CSS personalizado para um tema escuro e visual de cartões.
# Isso melhora significativamente a aparência padrão do Streamlit.
st.markdown("""
<style>
    /* * Estilos Gerais da Página
     * Define a cor de fundo e a cor do texto principal
     */
    .stApp {
        background-color: #0c0e14;
        color: #f1f1f1;
    }
    
    /* * Estilos de Título e Subtítulo
     * Centraliza e estiliza os títulos para uma aparência moderna
     */
    h1 {
        color: #e5e5e5;
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        letter-spacing: 1px;
    }
    
    h3 {
        color: #a0a0a0;
        text-align: center;
    }
    
    /* * Título de Categoria dentro do Card
     * Estilo específico para os títulos de cada seção de habilidades
     */
    .skills-card h2 {
        color: #7ab3ff;
        font-weight: 600;
        margin-bottom: 1.5em;
        text-align: center;
    }
    
    /* * Nome da Habilidade
     * Define a fonte e a cor para os nomes das habilidades
     */
    .skill-name {
        font-size: 1.1em;
        font-weight: 500;
        margin-bottom: 0.5em;
        color: #e5e5e5;
    }
    
    /* * Barra de Progresso
     * Altera a cor da barra de progresso para combinar com o tema
     */
    .stProgress > div > div > div > div {
        background-color: #7ab3ff;
    }
    
    /* * Rótulo do Progresso (o texto sobre a barra)
     * Define a cor do texto "Básico", "Intermediário", etc.
     */
    .stProgress .st-cr {
        color: #e5e5e5;
    }

    /* * Estilo para a Linha Separadora
     * Cria uma linha horizontal para separar as seções
     */
    hr {
        border-top: 1px solid #333;
        margin: 2em 0;
    }

</style>
""", unsafe_allow_html=True)

# --- Título Principal e Subtítulo ---
st.title('Habilidades Técnicas e Pessoais')
st.markdown("### Uma visão geral das minhas competências em diversas áreas.")
st.markdown("---")

# --- Dados das Habilidades ---
# Mapeia o nível de proficiência para um valor numérico para a barra de progresso.
# Isso facilita a conversão de texto para um valor que o Streamlit entende.
proficiency_map = {
    "Básico": 30,
    "Intermediário": 60,
    "Avançado": 90
}

# Lista de habilidades organizada por categoria.
# Esta estrutura de dados é a "fonte da verdade" para o conteúdo da página.
skills = {
    "Idiomas": [
        {"nome": "Inglês", "nivel": "Intermediário"}
    ],
    "Pacote Office": [
        {"nome": "Excel", "nivel": "Intermediário"},
        {"nome": "Power BI", "nivel": "Básico"},
        {"nome": "PowerPoint", "nivel": "Básico"},
        {"nome": "Word", "nivel": "Básico"}
    ],
    "Programação e Desenvolvimento": [
        {"nome": "JavaScript", "nivel": "Intermediário"},
        {"nome": "Java", "nivel": "Intermediário"},
        {"nome": "Python", "nivel": "Intermediário"},
        {"nome": "Arduino", "nivel": "Básico"},
        {"nome": "XML", "nivel": "Básico"},
        {"nome": "Back End", "nivel": "Básico"},
        {"nome": "Frontend", "nivel": "Básico"},
        {"nome": "CSS", "nivel": "Básico"},
        {"nome": "HTML", "nivel": "Básico"},
        {"nome": "Bootstrap", "nivel": "Básico"},
        {"nome": "Node.js", "nivel": "Básico"},
        {"nome": "JSON", "nivel": "Básico"},
        {"nome": "SQL", "nivel": "Básico"},
        {"nome": "SQL Server", "nivel": "Básico"},
        {"nome": "Oracle", "nivel": "Básico"},
        {"nome": "Banco de Dados", "nivel": "Básico"},
        {"nome": "Machine Learning", "nivel": "Básico"},
        {"nome": "React", "nivel": "Básico"},
    ],
    "Ferramentas e Plataformas": [
        {"nome": "Figma", "nivel": "Básico"},
        {"nome": "Maya", "nivel": "Básico"},
        {"nome": "Git", "nivel": "Básico"},
        {"nome": "SaaS", "nivel": "Básico"},
        {"nome": "Trello", "nivel": "Básico"},
        {"nome": "Windows", "nivel": "Básico"}
    ],
    "Metodologias e Soft Skills": [
        {"nome": "Metodologia Ágil", "nivel": "Básico"},
        {"nome": "Design Thinking", "nivel": "Básico"}
    ]
}

# --- Geração da Interface de Usuário (UI) para cada Categoria ---
for categoria, lista_habilidades in skills.items():
    # Cria um container para cada seção, permitindo agrupar os elementos
    with st.container():
        # Usa Markdown com HTML para criar o cartão de habilidades
        st.markdown(f'<div class="skills-card">', unsafe_allow_html=True)
        st.markdown(f'<h2>{categoria}</h2>', unsafe_allow_html=True)
        
        # Define o número de colunas para um layout mais organizado e responsivo.
        # Usa 2 colunas para categorias menores e 3 para a categoria de programação.
        if categoria in ["Pacote Office", "Ferramentas e Plataformas", "Metodologias e Soft Skills"]:
            num_columns = 2
        else:
            num_columns = 3
        
        cols = st.columns(num_columns)
        col_index = 0
        
        for habilidade in lista_habilidades:
            # Coloca cada habilidade na próxima coluna disponível
            with cols[col_index]:
                st.markdown(f'<p class="skill-name">{habilidade["nome"]}</p>', unsafe_allow_html=True)
                
                # Obtém o valor numérico do nível e cria a barra de progresso
                progress_value = proficiency_map.get(habilidade["nivel"], 0)
                st.progress(progress_value / 100, text=habilidade["nivel"])
                
            # Move para a próxima coluna, reiniciando na primeira quando o limite é atingido
            col_index = (col_index + 1) % num_columns
            
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("---")

