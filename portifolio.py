import streamlit as st


with st.sidebar:
    profileImage = st.image(".//assets//file.jpeg", width='content')
    st.markdown("# Michael Santos")
    st.markdown("### :red[● Sistemas de Informação]\n### :red[● Ciência de Dados]\n### :red[● Tec. em Eletrônica]\n")
    st.markdown("#### Localização\n:material/location_on: Sergipe, Brasil")

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







