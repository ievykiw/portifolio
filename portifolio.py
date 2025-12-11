# Importando a biblioteca streamlite e nomeando como st para as chamadas de função
import streamlit as st

# Configurações da página como título, icone e layout da página
st.set_page_config(
    page_title="Portfólio - Michael Santos",
    page_icon="",
    layout="wide"
)

# Definição da função modelo de Experiências Profissionais
def experienceModeler(experienceName, experienceLevel, experienceDateStart, experienceDateEnd, experienceDescription, experienceTools, experienceSkills):
    
    # Criação do container que irá conter a experiência a ser criada
    containerExperience = st.container(border=True)

    # Os parâmetros de Habilidades Adquiridas e Ferramentas Utilizadas recebem uma lista e a função abaixo une todos em uma única string
    # Cada um dos itens são badge únicos separados por espaço
    badgesTools = " ".join([f":red-badge[{ability}]" for ability in experienceTools])
    badgesSkills = " ".join([f":gray-badge[{ability}]" for ability in experienceSkills])

    # Construção do container com as informações da Experiência Profissional
    containerExperience.html(f"""<h1>{experienceName} - {experienceLevel}</h1>\n<p style="font-size: 1.2em">{experienceDescription}\n""")
    containerExperience.markdown(f"{badgesTools}\n\n{badgesSkills}\n\n Data Início: :red[{experienceDateStart}]  |   Data Fim: :red[{experienceDateEnd}]\n")

# Definição da função modelo de Projetos (Segue a mesma lógica da função experienceModeler)
def projectModeler(projectName, projectDate, projectDescription, projectTools, projectSkills):

    containerProject = st.container(border=True)

    badgesTools = " ".join([f":red-badge[{ability}]" for ability in projectTools])
    badgesSkills = " ".join([f":gray-badge[{ability}]" for ability in projectSkills])

    containerProject.html(f"""<h1>{projectName}</h1>\n<p style="font-size: 1.2em">{projectDescription}\n""")
    containerProject.markdown(f"{badgesTools}\n\n{badgesSkills}\n\n Realizado em: :red[{projectDate}]\n")


# Definição da função modelo de Eventos (Segue a mesma lógica da função experienceModeler e projectModeler, com apenas um adicional)
def eventModeler(eventName, eventDate, eventDescription, eventSkills, imageEventPath):
    
    containerEvent = st.container(border=True)
    
    badgesSkills = " ".join([f":gray-badge[{ability}]" for ability in eventSkills])

    containerEvent.html(f"""<h1>{eventName}</h1>\n<p style="font-size: 1.2em">{eventDescription}</p>""")
    containerEvent.markdown(f"{badgesSkills}\n\n Realizado em: :red[{eventDate}]\n")

    # Função para criação de um modal
    # Chamada do decorador que esperar uma função para definir o conteúdo do modal
    @st.dialog(f"{eventName}")

    # Defino uma função que irá receber o caminho da imagem, declarada no parâmetro imageEventPath da função eventModeler
    def eventImage():

        # Chamada da função image do streamlit com o caminho da imagem como argumento da função 
        st.image(imageEventPath)

    # Criação de um botão condicional, para abrir a imagem ao apertar o botão
    if st.button("Ver Foto", key=f"foto_{eventName}"): # Parâmetro key para gerar chaves únicas para cada imagem adicionada 
        
        # Chamada da função eventImage()
        eventImage()

# Definição da função modelo de Certificados
def certificationModeler(certificationTitle, certificationDate, certificationSource, imageCertificationPath):

    # Definição do container com o _with_ para que contemple todos os elementos incluindo a imagem que só aparece ao apertar o botão
    with st.container(border=True):
        st.html(f"""<h1>{certificationTitle} | {certificationSource}</h1>""")
        st.markdown(f"Realizado em: :red[{certificationDate}]")

        if st.button("Ver Certificado", key=f"btn_{certificationTitle}"):
            st.session_state[f"show_{certificationTitle}"] = True

        if st.session_state.get(f"show_{certificationTitle}", False):
            st.image(imageCertificationPath, width=700)
    
# Conteúdo textual da página, no geral utilizando linguagem markdown e html
with st.sidebar:
    profileImage = st.image(".//assets//CampusParty2025.jpeg", width='content', caption="Para ser grande, sê inteiro.")
    st.markdown("### ▶ Sistemas de Informação\n### ▶ Ciência de Dados\n### ▶ Tec. em Eletrônica\n")
    st.markdown("#### :material/location_on: Sergipe, Brasil")

    st.markdown("---")
    moreInfoOptions = ["Formação Acadêmica", "Línguas", "Contato"]

    # Criação dos botões de seleção de mais informações da sidebar
    selectMoreInfo = st.pills("# :material/more: Mais Informações", moreInfoOptions, selection_mode="single", default=moreInfoOptions[0])

    # Condições para definir quais informações o usuário quer acessar
    # Informação de Formação Acadêmica
    if (selectMoreInfo == 'Formação Acadêmica'):
        st.markdown("# :material/school: FORMAÇÕES ACADÊMICAS")
        st.markdown("# Graduando em Sistemas de Informação :orange-badge[:material/hourglass: Em Andamento]\n Universidade Federal de Sergipe - Campus São Cristóvão")  
        st.markdown("# Técnico em Eletrônica Integrado ao Ensino Médio :green-badge[:material/check: Concluído]\n Instituto Federal de Sergipe - Campus Aracaju")    
    
    # Informação de Línguas
    elif (selectMoreInfo == 'Línguas'):
        st.markdown("# :material/dictionary: LÍNGUAS")
        st.subheader("Inglês — B1+")
        st.progress(60)

        st.subheader("Espanhol — A2")
        st.progress(30)

        st.subheader("Português — Nativo")
        st.progress(100)

        st.markdown("_Referência: [QECR](https://www.efset.org/pt/cefr/)_")
    
    # Informação de Contato
    elif (selectMoreInfo == "Contato"):
        st.markdown("# :material/call: CONTATO")

        st.subheader(":material/mail: Email: michael4lves.pro@gmail.com")
        st.subheader(":material/business_center: LinkedIn: https://www.linkedin.com/in/michaeldssantos")
        st.subheader(":material/mobile_chat: Instagram: https://www.instagram.com/maicow.csv")

    st.markdown("---")

# Definição de colunas com a função _columns_ para dividir o "setor da página" em duas partes vertificais, como se houvessem 3 divs <div class="all"> <div class="left"><\div> <div class="right"><\div>  <\div>
col1, col2 = st.columns([0.7, 0.3]) # Definição do tamanho de cada coluna, sendo o máximo 100%, ou nesse caso 1

# Dentro da coluna 1:
with col1:
    st.html("""<h1 style="font-size: 3em; margin: 0"> Michael Santos </h1>""")
    st.html("<h1>Análise de Dados | Engenharia de Dados | Business Intelligence</h1>")
    st.html("""
                <p style="font-size: 1.2em">Atuo com Análise, Engenharia de Dados e BI, com foco no desenvolvimento de pipelines (ETL), afim otimizar fluxos de dados, desenvolver dashboards interativos e produzir relatórios estratégicos para o monitoramento de KPIs, gerando insights e apoiando as tomadas de decisão do negócio. Possuo experiência consolidada em Data Marketing e áreas correlatas.<p >
                """)
    st.markdown("---")

# Dentro da coluna 2:
with col2:
    st.html("""
        <h1>▶ Meus Repositórios:<h1>
        <p>
        ▶<a href="https://github.com/ievykiw" style="font-size: 20px; text-decoration: none; color: white; padding: 5px;"> GitHub </a>
                <br>
        ▶<a href="https://www.kaggle.com/ievykiw" style="font-size: 20px; text-decoration: none; color: white; padding: 5px;"> Kaggle </a>
        </p>
    """)


# Outro menu de opções, mas dessa vez com informações de Experiência Profissional, Projetos, Eventos e Ceritificados
workOptions = ["Experiência", "Projetos", "Eventos", "Certificações"]
workOptionsSelect = st.segmented_control("Selecione uma Opção", workOptions, selection_mode="single", default='Experiência') # Definição de tipo de seleção única e experiência profissional como valor padrão selecionado

# Informação de Experiência Profissional
if (workOptionsSelect == "Experiência"):
  experienceModeler("Lorem Ipsum 1", "Pleno", "09/2023", "01/2025", "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem IpsumLorem IpsumLorem IpsumLorem Ipsum Lorem Ipsum", ["Looker Studio", "Power BI", "CRM", "Automação"], ["Planejamento", "Execução"])
  experienceModeler("Lorem Ipsum 2", "Junior", "02/2021", "06/2022", "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem IpsumLorem IpsumLorem IpsumLorem Ipsum Lorem Ipsum", ["Excel", "Python", "SQL", "Pandas"], ["Visão de Negócio", "Produção"])

# Informação de Projetos
elif (workOptionsSelect == "Projetos"):
    projectModeler("Lorem Ipsum 1", "02/2024", "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem IpsumLorem IpsumLorem IpsumLorem Ipsum Lorem Ipsum",["Paint", ".NET", "Java"], ["Comunicação", "Liderança", "Gestão de Projetos"])

# Informação de Eventos
elif (workOptionsSelect == "Eventos"):
    eventModeler("Lorem Ipsum 1", "09/2023", "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem IpsumLorem IpsumLorem IpsumLorem Ipsum Lorem Ipsum", ["Comunicação", "Liderança", "Gestão de Projetos"], ".//assets//CampusParty2025.jpeg")
    eventModeler("Lorem Ipsum 2", "19/2025", "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem IpsumLorem IpsumLorem IpsumLorem Ipsum Lorem Ipsum", ["Comunicação", "Liderança", "Gestão de Projetos"], ".//assets//CampusParty2025.jpeg")

# Informação de Certificados
elif (workOptionsSelect == "Certificações"):
    certificationModeler("Lorem Ipsum 1", "09/2023", "OBR", ".//assets//OBREstadual.jpg")
    certificationModeler("Lorem Ipsum 2", "09/2023", "MIB", ".//assets//OBREstadual.jpg")
    certificationModeler("Lorem Ipsum 3", "09/2023", "UFS", ".//assets//OBREstadual.jpg")



