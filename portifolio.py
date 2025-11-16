import streamlit as st

st.set_page_config(
    page_title="Portfólio - Michael Santos",
    page_icon="",
    layout="wide"
)

def experienceModeler(experienceName, experienceLevel, experienceDateStart, experienceDateEnd, experienceDescription, experienceAbilities):
    containertExperience = st.container(border=True)
    badges = " ".join([f":red-badge[{ability}]" for ability in experienceAbilities])
    containertExperience.html(f"""<h1>{experienceName} - {experienceLevel}</h1>\n<p style="font-size: 1.2em">{experienceDescription}\n""")
    containertExperience.markdown(f"{badges}\n\n Data Início: :red[{experienceDateStart}]  |   Data Fim: :red[{experienceDateEnd}]\n")


with st.sidebar:
    profileImage = st.image(".//assets//file.jpeg", width='content', caption="Para ser grande, sê inteiro.")
    st.markdown("### >>> Sistemas de Informação\n### >>> Ciência de Dados\n### >>> Tec. em Eletrônica\n")

    st.markdown("---")
    moreInfoOptions = ["Formação Acadêmica", "Línguas", "Contato"]
    selectMoreInfo = st.pills("# :material/more: Mais Informações", moreInfoOptions, selection_mode="single", default=moreInfoOptions[0])

    if (selectMoreInfo == 'Formação Acadêmica'):
        st.markdown("# :material/school: FORMAÇÕES ACADÊMICAS")
        st.markdown("# Graduando em Sistemas de Informação :orange-badge[:material/hourglass: Em Andamento]\n Universidade Federal de Sergipe - Campus São Cristóvão")  
        st.markdown("# Técnico em Eletrônica Integrado ao Ensino Médio :green-badge[:material/check: Concluído]\n Instituto Federal de Sergipe - Campus Aracaju")    
    
    elif (selectMoreInfo == 'Línguas'):
        st.markdown("# :material/dictionary: LÍNGUAS")
        st.subheader("Inglês — B1+")
        st.progress(60)

        st.subheader("Espanhol — A2")
        st.progress(30)

        st.subheader("Português — Nativo")
        st.progress(100)

        st.markdown("_Referência: [QECR](https://www.efset.org/pt/cefr/)_")
    
    elif (selectMoreInfo == "Contato"):
        st.markdown("# :material/call: CONTATO")

    st.markdown("---")
    st.markdown("#### Localização\n:material/location_on: Sergipe, Brasil")

col1, col2 = st.columns([0.7, 0.3])

with col1:
    st.html("""<h1 style="font-size: 3em; margin: 0"> Michael Santos </h1>""")
    st.html("<h1>Análise de Dados | Engenharia de Dados | Business Intelligence</h1>")
    st.html("""
                <p style="font-size: 1.2em">Atuo com Análise, Engenharia de Dados e BI, com foco no desenvolvimento de pipelines (ETL), afim otimizar fluxos de dados, desenvolver dashboards interativos e produzir relatórios estratégicos para o monitoramento de KPIs, gerando insights e apoiando as tomadas de decisão do negócio. Possuo experiência consolidada em Data Marketing e áreas correlatas.<p >
                """)
    st.markdown("---")


with col2:
    st.html("""
        <h1>◌ Meus Repositórios:<h1>
        <p>
        >>><a href="https://github.com/ievykiw" style="font-size: 20px; text-decoration: none; color: white; padding: 5px;"> GitHub </a>
                <br>
        >>><a href="https://www.kaggle.com/ievykiw" style="font-size: 20px; text-decoration: none; color: white; padding: 5px;"> Kaggle </a>
        </p>
    """)


workOptions = ["Experiência", "Projetos", "Eventos", "Certificações"]
workOptionsSelect = st.segmented_control("Selecione uma Opção", workOptions, selection_mode="single", default='Experiência')

if (workOptionsSelect == "Experiência"):
  experienceModeler("Lorem Ipsum 1", "Pleno", "09/2023", "01/2025", "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem IpsumLorem IpsumLorem IpsumLorem Ipsum Lorem Ipsum", ["Looker Studio", "Power BI", "CRM", "Automação"])
  experienceModeler("Lorem Ipsum 2", "Junior", "02/2021", "06/2022", "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem IpsumLorem IpsumLorem IpsumLorem Ipsum Lorem Ipsum", ["Excel", "Python", "SQL", "Pandas"])

elif (workOptionsSelect == "Projetos"):
    st.markdown(f"Opção selecionada foi: {workOptionsSelect}")
elif (workOptionsSelect == "Eventos"):
    st.markdown(f"Opção selecionada foi: {workOptionsSelect}")
elif (workOptionsSelect == "Certificações"):
    st.markdown(f"Opção selecionada foi: {workOptionsSelect}")




