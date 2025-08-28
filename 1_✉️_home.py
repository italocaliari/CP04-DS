import streamlit as st
import os
from PIL import Image

# --- Configurações da Página ---
# A configuração da página deve ser a primeira chamada do Streamlit
st.set_page_config(
    page_title="Currículo Profissional",
    page_icon="📄",
    layout="wide"
)

# --- Estilos CSS Personalizados ---
# Aplica estilos para um visual mais limpo e profissional
st.markdown("""
<style>
    /* Estilos Gerais */
    .stApp {
        background-color: #0c0e14;
        color: #f1f1f1;
        font-family: 'Inter', sans-serif;
    }
    
    /* Título principal */
    h1 {
        color: #7ab3ff;
        text-align: center;
        font-weight: 700;
        letter-spacing: 1.5px;
    }

    /* Subtítulos de Seção */
    h2 {
        color: #e5e5e5;
        font-weight: 600;
        border-bottom: 2px solid #7ab3ff;
        padding-bottom: 5px;
        margin-top: 2em;
    }
    
    /* Estilo para a imagem de perfil */
    .profile-image {
        border-radius: 50%;
        border: 4px solid #7ab3ff;
        box-shadow: 0 0 15px rgba(122, 179, 255, 0.5);
    }
    
    /* Estilo para a lista de habilidades */
    .skills-list {
        list-style-type: none;
        padding: 0;
        margin: 0;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }
    
    .skill-item {
        background-color: #334d66;
        color: #fff;
        border-radius: 8px;
        padding: 8px 15px;
        font-size: 0.9em;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# --- Dados do Currículo Aprimorado ---

# O resumo foi reformulado para ser mais conciso e profissional, focando em objetivos e competências
RESUMO_PROFISSIONAL = "Futuro Engenheiro de Software com grande paixão por tecnologia e um compromisso inabalável com o aprendizado contínuo. Possuo uma base sólida em programação e busco aplicar meus conhecimentos para desenvolver soluções de software eficientes e inovadoras. Sou proativo, detalhista e altamente adaptável, com um forte interesse em contribuir para projetos desafiadores e crescer em um ambiente colaborativo e dinâmico."

# A seção de experiência profissional foi renomeada para "Objetivo Profissional" e otimizada
OBJETIVO_PROFISSIONAL = "Em busca de minha primeira oportunidade de estágio ou posição júnior na área de desenvolvimento de software. Desejo aplicar meus conhecimentos teóricos, contribuir com a equipe e absorver as melhores práticas do mercado, a fim de evoluir continuamente e agregar valor aos projetos da empresa."

# Dados de escolaridade
ESCOLARIDADE = [
    {
        "Instituicao": "FIAP",
        "Curso": "Engenharia de Software",
        "Periodo": "2024 - 2028",
        "Descricao": "Engenharia de Software é a área da computação dedicada à especificação, desenvolvimento, manutenção e criação de software, através da aplicação de tecnologias e práticas de gerenciamento de projetos e outras disciplinas, como a garantia de qualidade do software."
    }
]

# Dados de habilidades técnicas
HABILIDADES_TECNICAS = [
    "Python", "JavaScript", "HTML", "CSS", "SQL", "Git", "GitHub", "Metodologias Ágeis", "Resolução de Problemas", "Trabalho em Equipe"
]

# --- Layout da Página ---
st.title('Currículo Profissional')

# Foto de perfil e dados pessoais em colunas
col1, col2 = st.columns([1, 3], gap="large")

with col1:
    # Caminho para a imagem
    image_path = "imagens/minhafoto.jpg"
    
    # Verifica se o arquivo de imagem existe antes de tentar carregar
    if os.path.exists(image_path):
        st.image(image_path, 
                 caption="Sua Foto de Perfil", 
                 width=150)
    else:
        # Exibe um placeholder com uma mensagem de aviso caso a imagem não seja encontrada
        st.warning(f"Erro: Arquivo de imagem '{image_path}' não encontrado. Por favor, verifique o caminho e o nome do arquivo.")
        st.image("https://placehold.co/150x150/1a1e26/7ab3ff?text=Foto+Não+Encontrada", 
                 caption="Foto de Perfil Não Encontrada",
                 width=150)

with col2:
    st.markdown("#### **Nome:** Italo Caliari Silva")
    st.markdown("#### **Data de Nascimento:** 28/01/2006")
    st.markdown("#### **Email:** italo.caliari2006@gmail.com")
    st.markdown("#### **Telefone:** (11) 97237-3653")
    st.markdown("#### **LinkedIn:** https://www.linkedin.com/in/italocaliari")

# Resumo Profissional
st.header('Resumo Profissional')
# O texto do resumo agora é exibido sem o card, diretamente abaixo do cabeçalho
st.markdown(f'<div class="card"><p>{RESUMO_PROFISSIONAL}</p></div>', unsafe_allow_html=True)

# Objetivo Profissional (antiga Experiência Profissional)
st.header('Objetivo Profissional')
st.markdown(f'<div class="card"><p>{OBJETIVO_PROFISSIONAL}</p></div>', unsafe_allow_html=True)

# Escolaridade
st.header('Escolaridade')
# Constrói o texto da escolaridade a partir da lista de dados
escolaridade_markdown = ""
for item in ESCOLARIDADE:
    escolaridade_markdown += f"**Instituição:** {item['Instituicao']}<br>"
    escolaridade_markdown += f"**Curso:** {item['Curso']}<br>"
    escolaridade_markdown += f"**Período:** {item['Periodo']}<br>"
    escolaridade_markdown += f"**Descrição:** {item['Descricao']}<br>"

st.markdown(f'<div class="card"><p>{escolaridade_markdown}</p></div>', unsafe_allow_html=True)