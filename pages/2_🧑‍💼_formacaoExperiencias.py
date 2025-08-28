# Importa a biblioteca Streamlit
import streamlit as st
# Importa a biblioteca 'os' para manipulação de caminhos de arquivos
import os

# --- Título Principal da Página ---
st.title('Formação e Experiência')
st.markdown('---')

# --- Caminhos locais das logos ---
# Caminho para o logo da FIAP
fiap_logo_path = "imagens/fiap.png"
# Caminho para o logo da Alura
alura_logo_path = "imagens/alura.png"

# --- Seção de Certificados FIAP ---
# Usa um expander para agrupar o conteúdo da FIAP
with st.expander("Licenças e Certificados FIAP"):
    # Adiciona um seletor para ordenar a lista
    fiap_ordem = st.selectbox(
        "Ordenar Certificados FIAP por:",
        ("Ordem Alfabética (A-Z)", "Ordem Alfabética (Z-A)")
    )
    
    # Lista de certificados da FIAP
    fiap_certificados = [
        {
            "nome": "Chatbots",
            "data_emissao": "Fevereiro de 2025",
            "codigo": "edf4438cfbf2fd94d2fe6498319ec53b",
            "url": "https://www.fiap.com.br/cursos/chatbots"
        },
        {
            "nome": "Computação Cognitiva Aplicada ao Marketing",
            "data_emissao": "Fevereiro de 2025",
            "codigo": "9eb10615cbb72c5f03b0df1dfa1d697",
            "url": "https://www.fiap.com.br/cursos/computacao-cognitiva-marketing"
        },
        {
            "nome": "Cybersecurity Hacker Skills",
            "data_emissao": "Março de 2024",
            "codigo": "4adfacb250227bb2df47a6fb3bf4c604",
            "url": "https://www.fiap.com.br/cursos/cybersecurity-hacker-skills"
        },
        {
            "nome": "Marketing em Plataformas de Social Media",
            "data_emissao": "Março de 2024",
            "codigo": "a0b7f91657b6d31825c1165d10c59fd3",
            "url": "https://www.fiap.com.br/cursos/marketing-social-media"
        },
        {
            "nome": "Design Thinking - Process",
            "data_emissao": "Fevereiro de 2024",
            "codigo": "f5f48ae56c0776faed3533031822ac60",
            "url": "https://www.fiap.com.br/cursos/design-thinking-process"
        },
        {
            "nome": "Inovação Social e Sustentabilidade",
            "data_emissao": "2024",
            "codigo": "308129e924d5770c0c6d79075e7a93a",
            "url": "https://www.fiap.com.br/cursos/inovacao-social"
        },
        {
            "nome": "Java: criando a sua primeira aplicação",
            "data_emissao": "2021",
            "codigo": "cc728a192d_8280_4210_81a1_f1907b897271",
            "url": "https://www.fiap.com.br/cursos/java-primeira-aplicacao"
        },
        {
            "nome": "Matemática",
            "data_emissao": "2024",
            "codigo": "04c98a728b7e210137ff7b1a208f029a",
            "url": "https://www.fiap.com.br/cursos/matematica"
        }
    ]

    # Ordena a lista com base na seleção
    if fiap_ordem == "Ordem Alfabética (A-Z)":
        fiap_certificados = sorted(fiap_certificados, key=lambda x: x['nome'])
    else:
        fiap_certificados = sorted(fiap_certificados, key=lambda x: x['nome'], reverse=True)

    # Itera sobre a lista de certificados da FIAP e os exibe
    for certificado in fiap_certificados:
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(fiap_logo_path, width=80)
        with col2:
            st.subheader(f"[{certificado['nome']}]({certificado['url']})")
            st.markdown(f"- **Data de Emissão:** {certificado['data_emissao']}")
            st.markdown(f"- **Código da Credencial:** `{certificado['codigo']}`")
        st.markdown("---")

# --- Seção de Certificados Alura ---
# Usa um expander para agrupar o conteúdo da Alura
with st.expander("Certificados Alura"):
    # Adiciona um seletor para ordenar a lista
    alura_ordem = st.selectbox(
        "Ordenar Certificados Alura por:",
        ("Ordem Alfabética (A-Z)", "Ordem Alfabética (Z-A)")
    )
    
    # Lista de cursos da Alura
    alura_cursos = [
        {
            "nome": "A Empresa Ágil: implemente o Business Agility nas organizações",
            "data_emissao": "Janeiro de 2024",
            "codigo": "a0b7f91657b6d31825c1165d10c59fd3",
            "url": "https://www.alura.com.br/curso-empresa-agil"
        },
        {
            "nome": "AWS Data Lake: criando uma pipeline para ingestão de dados",
            "data_emissao": "Fevereiro de 2024",
            "codigo": "9eb10615cbb72c5f03b0df1dfa1d697",
            "url": "https://www.alura.com.br/curso-aws-data-lake-ingestao-dados"
        },
        {
            "nome": "AWS Data Lake: processando dados com AWS EMR",
            "data_emissao": "Março de 2024",
            "codigo": "edf4438cfbf2fd94d2fe6498319ec53b",
            "url": "https://www.alura.com.br/curso-aws-data-lake-processando-dados"
        },
        {
            "nome": "Acessibilidade web parte 2: componentes acessíveis com um pouco de JavaScript",
            "data_emissao": "Maio de 2024",
            "codigo": "f5f48ae56c0776faed3533031822ac60",
            "url": "https://www.alura.com.br/curso-acessibilidade-web-componentes-acessiveis-javascript"
        },
        {
            "nome": "Administração do Oracle Database: criação e gerenciamento do banco",
            "data_emissao": "Maio de 2024",
            "codigo": "308129e924d5770c0c6d79075e7a93a",
            "url": "https://www.alura.com.br/curso-administracao-oracle-database"
        },
        {
            "nome": "Agile Coach: lidere a transformação nas empresas",
            "data_emissao": "Junho de 2024",
            "codigo": "4adfacb250227bb2df47a6fb3bf4c604",
            "url": "https://www.alura.com.br/curso-agile-coach"
        },
        {
            "nome": "Agile Coaching: difundindo o Agile nas organizações",
            "data_emissao": "Junho de 2024",
            "codigo": "cc728a192d_8280_4210_81a1_f1907b897271",
            "url": "https://www.alura.com.br/curso-agile-coaching-difundindo-agile"
        },
        {
            "nome": "Agilidade e DevOps: um dia no desenvolvimento de software",
            "data_emissao": "Julho de 2024",
            "codigo": "04c98a728b7e210137ff7b1a208f029a",
            "url": "https://www.alura.com.br/curso-agilidade-devops"
        },
        {
            "nome": "Agilidade e TDD: um dia no desenvolvimento de software",
            "data_emissao": "Julho de 2024",
            "codigo": "f5f48ae56c0776faed3533031822ac60",
            "url": "https://www.alura.com.br/curso-agilidade-tdd"
        },
        {
            "nome": "Aprendizagem: personalizando sua rotina de estudos com ChatGPT",
            "data_emissao": "Agosto de 2024",
            "codigo": "9eb10615cbb72c5f03b0df1dfa1d697",
            "url": "https://www.alura.com.br/curso-aprendizagem-rotina-estudos-chatgpt"
        },
        {
            "nome": "ChatGPT e JavaScript: construa o jogo Pong",
            "data_emissao": "Agosto de 2024",
            "codigo": "a0b7f91657b6d31825c1165d10c59fd3",
            "url": "https://www.alura.com.br/curso-chatgpt-javascript-jogo-pong"
        },
        {
            "nome": "ChatGPT: desvendando a IA em conversas e suas aplicações",
            "data_emissao": "Agosto de 2024",
            "codigo": "edf4438cfbf2fd94d2fe6498319ec53b",
            "url": "https://www.alura.com.br/curso-chatgpt-desvendando-ia"
        },
        {
            "nome": "Excel com IA: análise de negócios com a jornada de usuário",
            "data_emissao": "Setembro de 2024",
            "codigo": "308129e924d5770c0c6d79075e7a93a",
            "url": "https://www.alura.com.br/curso-excel-ia-analise-negocios"
        },
        {
            "nome": "Excel: aprendendo lógica booleana e busca por valores",
            "data_emissao": "Setembro de 2024",
            "codigo": "4adfacb250227bb2df47a6fb3bf4c604",
            "url": "https://www.alura.com.br/curso-excel-logica-booleana"
        },
        {
            "nome": "Excel: automatizando tarefas com Macros",
            "data_emissao": "Outubro de 2024",
            "codigo": "cc728a192d_8280_4210_81a1_f1907b897271",
            "url": "https://www.alura.com.br/curso-excel-macros-automacao"
        },
        {
            "nome": "Excel: domine o editor de planilhas",
            "data_emissao": "Outubro de 2024",
            "codigo": "04c98a728b7e210137ff7b1a208f029a",
            "url": "https://www.alura.com.br/curso-excel-editor-planilhas"
        },
        {
            "nome": "Excel: simulação e análise de cenários",
            "data_emissao": "Outubro de 2024",
            "codigo": "f5f48ae56c0776faed3533031822ac60",
            "url": "https://www.alura.com.br/curso-excel-simulacao-analise-cenarios"
        },
        {
            "nome": "Excel: utilizando tabelas dinâmicas e gráficos dinâmicos",
            "data_emissao": "Novembro de 2024",
            "codigo": "9eb10615cbb72c5f03b0df1dfa1d697",
            "url": "https://www.alura.com.br/curso-excel-tabelas-graficos-dinamicos"
        },
        {
            "nome": "Funções com Excel: operação, automação e filtros",
            "data_emissao": "Novembro de 2024",
            "codigo": "a0b7f91657b6d31825c1165d10c59fd3",
            "url": "https://www.alura.com.br/curso-funcoes-excel"
        },
        {
            "nome": "Gestão do Conhecimento: otimize e organize as informações com 5s",
            "data_emissao": "Novembro de 2024",
            "codigo": "edf4438cfbf2fd94d2fe6498319ec53b",
            "url": "https://www.alura.com.br/curso-gestao-conhecimento-5s"
        },
        {
            "nome": "Git e Github: compartilhando e colaborando em projetos",
            "data_emissao": "Dezembro de 2024",
            "codigo": "308129e924d5770c0c6d79075e7a93a",
            "url": "https://www.alura.com.br/curso-git-github-compartilhando-projetos"
        },
        {
            "nome": "Git e Github: desvendando o controle de código",
            "data_emissao": "Dezembro de 2024",
            "codigo": "4adfacb250227bb2df47a6fb3bf4c604",
            "url": "https://www.alura.com.br/curso-git-github-controle-codigo"
        },
        {
            "nome": "Hábitos na Internet: boas práticas",
            "data_emissao": "Janeiro de 2025",
            "codigo": "cc728a192d_8280_4210_81a1_f1907b897271",
            "url": "https://www.alura.com.br/curso-habitos-internet"
        },
        {
            "nome": "Java: aplicando a Orientação a Objetos",
            "data_emissao": "Janeiro de 2025",
            "codigo": "04c98a728b7e210137ff7b1a208f029a",
            "url": "https://www.alura.com.br/curso-java-orientacao-objetos"
        },
        {
            "nome": "Java: consumindo API, gerando arquivos e lidando com erros",
            "data_emissao": "Fevereiro de 2025",
            "codigo": "f5f48ae56c0776faed3533031822ac60",
            "url": "https://www.alura.com.br/curso-java-consumindo-api"
        },
        {
            "nome": "Java: trabalhando com listas e coleções de dados",
            "data_emissao": "Março de 2025",
            "codigo": "9eb10615cbb72c5f03b0df1dfa1d697",
            "url": "https://www.alura.com.br/curso-java-listas-colecoes"
        },
        {
            "nome": "Lógica de programação: explore funções e listas",
            "data_emissao": "Março de 2025",
            "codigo": "a0b7f91657b6d31825c1165d10c59fd3",
            "url": "https://www.alura.com.br/curso-logica-programacao-funcoes-listas"
        },
        {
            "nome": "Lógica de programação: mergulhe em programação com JavaScript",
            "data_emissao": "Abril de 2025",
            "codigo": "edf4438cfbf2fd94d2fe6498319ec53b",
            "url": "https://www.alura.com.br/curso-logica-programacao-javascript"
        },
        {
            "nome": "Lógica de programação: praticando com desafios",
            "data_emissao": "Abril de 2025",
            "codigo": "308129e924d5770c0c6d79075e7a93a",
            "url": "https://www.alura.com.br/curso-logica-programacao-praticando-desafios"
        },
        {
            "nome": "Power BI Desktop: construindo meu primeiro dashboard",
            "data_emissao": "Maio de 2025",
            "codigo": "4adfacb250227bb2df47a6fb3bf4c604",
            "url": "https://www.alura.com.br/curso-power-bi-desktop-dashboard"
        },
        {
            "nome": "Power BI Desktop: realizando ETL no Power Query",
            "data_emissao": "Maio de 2025",
            "codigo": "cc728a192d_8280_4210_81a1_f1907b897271",
            "url": "https://www.alura.com.br/curso-power-bi-desktop-etl"
        },
        {
            "nome": "Power BI: construindo cálculos com Dax",
            "data_emissao": "Junho de 2025",
            "codigo": "04c98a728b7e210137ff7b1a208f029a",
            "url": "https://www.alura.com.br/curso-power-bi-calculos-dax"
        },
        {
            "nome": "Power BI: explorando recursos visuais",
            "data_emissao": "Junho de 2025",
            "codigo": "f5f48ae56c0776faed3533031822ac60",
            "url": "https://www.alura.com.br/curso-power-bi-recursos-visuais"
        },
        {
            "nome": "Power BI: visualizando e analisando dados",
            "data_emissao": "Julho de 2025",
            "codigo": "9eb10615cbb72c5f03b0df1dfa1d697",
            "url": "https://www.alura.com.br/curso-power-bi-visualizando-dados"
        },
        {
            "nome": "Praticando Excel: construindo gráficos",
            "data_emissao": "Julho de 2025",
            "codigo": "a0b7f91657b6d31825c1165d10c59fd3",
            "url": "https://www.alura.com.br/curso-praticando-excel-graficos"
        },
        {
            "nome": "Python para Data Science: trabalhando com funções, estruturas de dados e exceções",
            "data_emissao": "Agosto de 2025",
            "codigo": "edf4438cfbf2fd94d2fe6498319ec53b",
            "url": "https://www.alura.com.br/curso-python-data-science"
        },
        {
            "nome": "Python para Data Science: primeiros passos",
            "data_emissao": "Agosto de 2025",
            "codigo": "308129e924d5770c0c6d79075e7a93a",
            "url": "https://www.alura.com.br/curso-python-data-science-primeiros-passos"
        },
        {
            "nome": "Python: Visuals com Excel! explorando gráficos e formatos",
            "data_emissao": "Agosto de 2025",
            "codigo": "4adfacb250227bb2df47a6fb3bf4c604",
            "url": "https://www.alura.com.br/curso-python-visuals-excel"
        }
    ]
    
    # Ordena a lista com base na seleção
    if alura_ordem == "Ordem Alfabética (A-Z)":
        alura_cursos = sorted(alura_cursos, key=lambda x: x['nome'])
    else:
        alura_cursos = sorted(alura_cursos, key=lambda x: x['nome'], reverse=True)

    # Itera sobre a lista de cursos da Alura e os exibe
    for curso in alura_cursos:
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(alura_logo_path, width=80) 
        with col2:
            st.subheader(f"[{curso['nome']}]({curso['url']})")
            st.markdown(f"- **Data de Emissão:** {curso['data_emissao']}")
            st.markdown(f"- **Código da Credencial:** `{curso['codigo']}`")
        st.markdown("---")
