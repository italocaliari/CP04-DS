# Importa a biblioteca Streamlit
import streamlit as st
import os

# --- Configurações da Página e Tema Personalizado ---
# Configura o layout da página para ser mais amplo
st.set_page_config(layout="wide", page_title="Meus Desafios")

# Aplica CSS personalizado para um tema escuro e visual de cartões
st.markdown("""
<style>
    /* Estilo geral da página */
    .stApp {
        background-color: #0c0e14;
        color: #f1f1f1;
    }
    
    /* Título principal */
    .stApp > header {
        background-color: transparent;
    }
    h1 {
        color: #e5e5e5;
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        letter-spacing: 1px;
    }
    
    /* Subtítulo */
    h3 {
        color: #a0a0a0;
        text-align: center;
    }
 
    /* Título do projeto */
    .project-card h2 {
        color: #7ab3ff;
        font-weight: 600;
        margin-bottom: 0.5em;
    }

    /* Descrição do projeto */
    .project-card p {
        color: #c1c1c1;
        margin-top: 0;
    }
    
    /* Estilo para o botão */
    .stButton > button {
        background-color: #2e3542;
        color: #ffffff;
        border: 1px solid #4a5461;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.2s ease-in-out;
    }
    
    .stButton > button:hover {
        background-color: #4a5461;
        border-color: #7ab3ff;
        color: #7ab3ff;
    }

    /* Estilo para a imagem do projeto */
    .stImage img {
        border-radius: 8px;
        width: 100%;
        height: 100%; /* Ajuste para preencher a altura */
        object-fit: cover; /* Recorta a imagem para se ajustar ao contêiner */
    }

    /* Estilo para a imagem do EcoAlert (quadrado) */
    .ecoalert-image img {
        width: 250px;
        height: 250px;
        object-fit: contain; /* Garante que a imagem inteira seja visível */
        background-color: #0d121c; /* Fundo escuro para a imagem */
        border: 2px solid #5cb85c;
        border-radius: 12px;
    }

    /* Estilo para a imagem da Melodia (retangular) */
    .melodia-image img {
        width: 350px;
        height: 200px;
        object-fit: cover;
        border-radius: 12px;
        box-shadow: 0 0 15px rgba(122, 179, 255, 0.3); /* Sombra azul clara */
    }

    /* Estilo para a imagem do Simulador de F1 (retangular com borda) */
    .f1-image img {
        width: 350px;
        height: 200px;
        object-fit: cover;
        border: 2px solid #ff4500; /* Borda laranja */
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(255, 69, 0, 0.5);
    }
    
    /* Estilo para o separador */
    hr {
        border-top: 1px solid #333;
        margin: 2em 0;
    }

</style>
""", unsafe_allow_html=True)

# --- Título Principal e Subtítulo ---
st.title('Meus Desafios e Projetos')
st.markdown("### Projetos e desafios desenvolvidos em equipe.", unsafe_allow_html=True)
st.markdown("---")

# --- Dados dos Projetos ---
# Agora usaremos os nomes de arquivo baseados na sua estrutura de pastas.
# O caminho é assumido como "imagens/<nome_do_arquivo>".
projetos = [
    {
        "titulo": "EcoAlert",
        "descricao": "Projeto de monitoramento ambiental desenvolvido em equipe, focado na criação de uma aplicação para acompanhar dados ambientais. Apresentado como parte de um desafio.",
        "link": "https://www.linkedin.com/posts/rafaelmmaniezo_ecoalert-ugcPost-7348339663687901184-WdiL",
        "imagem_url": os.path.join("imagens", "ecoalert.png")
    },
    {
        "titulo": "Melodia",
        "descricao": "Desenvolvimento de uma landing page para um projeto de empresa de tecnologia.",
        "link": "https://www.linkedin.com/posts/rafaelmmaniezo_desenvolvimentoweb-frontend-javascript-ugcPost-7294432833995968512-hAUQ",
        "imagem_url": os.path.join("imagens", "melodia.png")
    },
    {
        "titulo": "Simulador de Fórmula 1",
        "descricao": "Projeto de Engenharia de Software que consistiu na criação de um simulador de corrida. O projeto utilizou dados de telemetria para a criação de gráficos e visualização de dados.",
        "link": "https://www.linkedin.com/posts/leandro-souza-326722181_engenhariadesoftware-challenge-automobilismo-ugcPost-7287589490200563712-eAfb",
        "imagem_url": os.path.join("imagens", "hitrace.png")
    }
]

# --- Geração da UI para os projetos ---
for projeto in projetos:
    with st.container():
        st.markdown(f'<div class="project-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([2, 3])
        
        with col1:
            # Exibe a imagem do projeto com estilos personalizados
            if projeto["titulo"] == "EcoAlert":
                st.markdown(f'<div class="ecoalert-image">', unsafe_allow_html=True)
                st.image(projeto["imagem_url"])
                st.markdown('</div>', unsafe_allow_html=True)
            elif projeto["titulo"] == "Melodia":
                st.markdown(f'<div class="melodia-image">', unsafe_allow_html=True)
                st.image(projeto["imagem_url"])
                st.markdown('</div>', unsafe_allow_html=True)
            elif projeto["titulo"] == "Simulador de Fórmula 1":
                st.markdown(f'<div class="f1-image">', unsafe_allow_html=True)
                st.image(projeto["imagem_url"])
                st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            # Exibe o título, descrição e link
            st.markdown(f'<h2>{projeto["titulo"]}</h2>', unsafe_allow_html=True)
            st.markdown(f'<p>{projeto["descricao"]}</p>', unsafe_allow_html=True)
            st.markdown(f'[Ver no LinkedIn]({projeto["link"]})', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("---")
