#libraries
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import plotly.graph_objects as go
#from urllib.error import URLError
#DÚVIDAS
rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQQNWj747l2uR_TOZ_4cTnajPMmbpLb84ILH1KMzu1eN3BwalrUTuN7XrcWWU6q5qVGnw-Ay4QEG1x_/pub?gid=1381735194&single=true&output=csv')
dataD = rD.content
dfD = pd.read_csv(BytesIO(dataD), index_col=0)
NregD = len(dfD)
dfD.columns = ['equipe', 'nome', 'duvida', 'obs']
#============================================================================================
#IMPORTAÇÃO DOS DADOS DA PLANILHA Pontuação das Equipes II Hackathon Mackenzie-Logithink-IMA (hackathon.cct.2023@gmail.com)
rP = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQj4zhEz_COCvFMKnizUaRZz87rl8tOVv3b-U7q9fQFMauMRbT7vJDIlI8HPSLAdoCsthRh6yEigLsX/pub?gid=87278842&single=true&output=csv')
dataP = rP.content
dfP = pd.read_csv(BytesIO(dataP))
dfP.columns = ['D/H', 'Participacao', 'Criatividade', 'Coerencia', 'Apresentacao', 'MVP', 'Inovacao', 'OBS', 'Equipe']
resumo = dfP.groupby(["Equipe"]).sum()
rotulo = resumo.index
nEquipes = len(rotulo)
qtdDadosPorEquipe = []
for count in range(nEquipes):
  selecao01P = dfP['Equipe']==rotulo[count]
  df01P = dfP[selecao01P]
  qtdDadosPorEquipe.append(len(df01P))
  del(df01P)

resumo = dfP.groupby(["Equipe"]).sum()
dfresumo = pd.DataFrame(resumo)
n=len(rotulo)
#============================================================================================
selecao01D = dfD['equipe']=='Equipe 01'
df01D = dfD[selecao01D]
selecao02D = dfD['equipe']=='Equipe 02'
df02D = dfD[selecao02D]
selecao03D = dfD['equipe']=='Equipe 03'
df03D = dfD[selecao03D]
selecao04D = dfD['equipe']=='Equipe 04'
df04D = dfD[selecao04D]
selecao05D = dfD['equipe']=='Equipe 05'
df05D = dfD[selecao05D]
selecao06D = dfD['equipe']=='Equipe 06'
df06D = dfD[selecao06D]
selecao07D = dfD['equipe']=='Equipe 07'
df07D = dfD[selecao07D]
selecao08D = dfD['equipe']=='Equipe 08'
df08D = dfD[selecao08D]
selecao09D = dfD['equipe']=='Equipe 09'
df09D = dfD[selecao09D]
selecao10D = dfD['equipe']=='Equipe 10'
df10D = dfD[selecao10D]
selecao11D = dfD['equipe']=='Equipe 11'
df11D = dfD[selecao11D]
selecao12D = dfD['equipe']=='Equipe 12'
df12D = dfD[selecao12D]
selecao13D = dfD['equipe']=='Equipe 13'
df13D = dfD[selecao13D]
selecao14D = dfD['equipe']=='Equipe 14'
df14D = dfD[selecao14D]
selecao15D = dfD['equipe']=='Equipe 15'
df15D = dfD[selecao15D]

# eliminar as colunas com valores ausentes
summary = dfD.dropna(subset=['duvida'], axis=0)['duvida']
# concatenar as palavras
all_summary = " ".join(s for s in summary)
# lista de stopword
stopwords = set(STOPWORDS)
stopwords.update(["Qual", "qual", "que", "Que", "de", "ao", "o", "nao", "para", "da", "meu", "em", "você", "ter", "um", "uma", "ou", "os", "ser", "só"])
# gerar uma wordcloud
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="white",
                      width=1600, height=800).generate(all_summary)
# mostrar a imagem final
#fig, ax = plt.subplots(figsize=(10,6))
#ax.imshow(wordcloud, interpolation='bilinear')
#ax.set_axis_off()
plt.imshow(wordcloud);
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
#st.pyplot()
wordcloud.to_file("Nuvem_de_Palavras_DUVIDAS.png")

#RESPOSTAS
rR = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTIxe7VmjCRpyVvwKaajuRFyp6T1MRGOx_GCUg7ghiA2QWbiNLYam-xpLYhXE2Gdn6RgLjRRJPD4WZ-/pub?gid=1131399848&single=true&output=csv')
dataR = rR.content
dfR = pd.read_csv(BytesIO(dataR), index_col=0)
NregR = len(dfR)
dfR.columns = ['enderecoMAIL', 'equipe', 'nome', 'resposta', 'observacao', 'mail']

selecao01R = dfR['equipe']=='Equipe 01'
df01R = dfR[selecao01R]
selecao02R = dfR['equipe']=='Equipe 02'
df02R = dfR[selecao02R]
selecao03R = dfR['equipe']=='Equipe 03'
df03R = dfR[selecao03R]
selecao04R = dfR['equipe']=='Equipe 04'
df04R = dfR[selecao04R]
selecao05R = dfR['equipe']=='Equipe 05'
df05R = dfR[selecao05R]
selecao06R = dfR['equipe']=='Equipe 06'
df06R = dfR[selecao06R]
selecao07R = dfR['equipe']=='Equipe 07'
df07R = dfR[selecao07R]
selecao08R = dfR['equipe']=='Equipe 08'
df08R = dfR[selecao08R]
selecao09R = dfR['equipe']=='Equipe 09'
df09R = dfR[selecao09R]
selecao10R = dfR['equipe']=='Equipe 10'
df10R = dfR[selecao10R]
selecao11R = dfR['equipe']=='Equipe 11'
df11R = dfR[selecao11R]
selecao12R = dfR['equipe']=='Equipe 12'
df12R = dfR[selecao12R]
selecao13R = dfR['equipe']=='Equipe 13'
df13R = dfR[selecao13R]
selecao14R = dfR['equipe']=='Equipe 14'
df14R = dfR[selecao14R]
selecao15R = dfR['equipe']=='Equipe 15'
df15R = dfR[selecao15R]

#Cálculo do Número de Registros por EQUIPE
NregDf01D = len(df01D)
NregDf01R = len(df01R)
NregDf02D = len(df02D)
NregDf02R = len(df02R)
NregDf03D = len(df03D)
NregDf03R = len(df03R)
NregDf04D = len(df04D)
NregDf04R = len(df04R)
NregDf05D = len(df05D)
NregDf05R = len(df05R)
NregDf06D = len(df06D)
NregDf06R = len(df06R)
NregDf07D = len(df07D)
NregDf07R = len(df07R)
NregDf08D = len(df08D)
NregDf08R = len(df08R)
NregDf09D = len(df09D)
NregDf09R = len(df09R)
NregDf10D = len(df10D)
NregDf10R = len(df10R)
NregDf11D = len(df11D)
NregDf11R = len(df11R)
NregDf12D = len(df12D)
NregDf12R = len(df12R)
NregDf13D = len(df13D)
NregDf13R = len(df13R)
NregDf14D = len(df14D)
NregDf14R = len(df14R)
NregDf15D = len(df15D)
NregDf15R = len(df15R)

image01 = Image.open('ImagemLateral.jpg')
st.sidebar.image(image01, width=300, caption='Mack Week CCT 2022') 
#st.title("PAINEL - EQUIPES HACKATHON")
Titulo_Principal = '<p style="font-weight: bolder; color:DarkBlue; font-size: 32px;">2ª EDIÇÃO DO DESAFIO HACKATHON: MACKENZIE CAMPINAS - LOGITHINK.IT - IMA (Edição 2023)</p>'
st.markdown(Titulo_Principal, unsafe_allow_html=True)
mystyle1 =   '''<style> p{text-align:center;}</style>'''
st.markdown(mystyle1, unsafe_allow_html=True) 

# st.header("Cabeçalho")
#st.subheader("Sub Cabeçalho")
#st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")
menu = ["Dúvidas",
        "Respostas",
        "Dúvidas e Respostas",
        "Pontos Equipes",
        "EQUIPE 01",
        "EQUIPE 02",
        "EQUIPE 03", 
        "EQUIPE 04",
        "EQUIPE 05",
        "EQUIPE 06",
        "EQUIPE 07",
        "EQUIPE 08",
        "EQUIPE 09",
        "EQUIPE 10",
        "EQUIPE 11",
        "EQUIPE 12",
        "EQUIPE 13",
        "EQUIPE 14",
        "EQUIPE 15"]
choice = st.sidebar.selectbox("Menu de Opções",menu)
st.sidebar.info("Web app desenvolvido pelo professor Massaki de O. Igarashi para a gestão e acompanhamento do envio de dúvidas e respostas entre alunos, tutores, mentores e professores.")
st.sidebar.info("2ª EDIÇÃO DO DESAFIO HACKATHON: MACKENZIE CAMPINAS - LOGITHINK.IT - IMA (Edição 2023)")
if choice == "Dúvidas": 
    st.header("Painel Analítico: DÚVIDAS")   
    st.write('EQUIPE 01:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df01D['duvida']) 
    nD = len(df01D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df01D['duvida'][i]) 
    st.write('EQUIPE 02:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df02D['duvida']) 
    nD = len(df02D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df02D['duvida'][i]) 
    st.write('EQUIPE 03:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df03D['duvida'])
    nD = len(df03D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df03D['duvida'][i]) 
    st.write('EQUIPE 04:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df04D['duvida']) 
    nD = len(df04D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df04D['duvida'][i]) 
    st.write('EQUIPE 05:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df05D['duvida']) 
    nD = len(df05D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df05D['duvida'][i]) 
    st.write('EQUIPE 06:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df06D['duvida'])
    nD = len(df06D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df06D['duvida'][i]) 
    st.write('EQUIPE 07:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df07D['duvida']) 
    nD = len(df07D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df07D['duvida'][i]) 
    st.write('EQUIPE 08:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df08D['duvida']) 
    nD = len(df08D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df08D['duvida'][i]) 
    st.write('EQUIPE 09:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df09D['duvida']) 
    nD = len(df09D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df09D['duvida'][i]) 
    st.write('EQUIPE 10:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df10D['duvida']) 
    nD = len(df10D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df10D['duvida'][i]) 
    st.write('EQUIPE 11:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df11D['duvida']) 
    nD = len(df11D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df11D['duvida'][i]) 
    st.write('EQUIPE 12:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df12D['duvida']) 
    nD = len(df12D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df12D['duvida'][i]) 
    st.write('EQUIPE 13:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df13D['duvida']) 
    nD = len(df13D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df13D['duvida'][i]) 
    st.write('EQUIPE 14:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df14D['duvida'])
    nD = len(df14D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df14D['duvida'][i]) 
    st.write('EQUIPE 15:')
    st.warning('Dúvida(s) Enviada(s)')
    #st.write(df15D['duvida'])
    nD = len(df15D['duvida'])
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(df15D['duvida'][i]) 
    st.subheader("HISTÓRICO DE DÚVIDAS: ")
    
    #st.write(dfD['equipe'] + ":" + dfD['duvida'])
    nD = len(dfD)
    for i in range(nD):
      with st.chat_message("user"):   
        st.write(dfD['equipe'][i] + ":" + dfD['duvida'][i]) 
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
elif choice == "Respostas":       
    st.header("Painel Analítico: RESPOSTAS")    
    st.write('EQUIPE 01:')    
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df01R['resposta'])
    nR = len(df01R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df01R['resposta'][j])
    st.write('EQUIPE 02:')    
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df02R['resposta'])
    nR = len(df02R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df02R['resposta'][j])
    st.write('EQUIPE 03:')    
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df03R['resposta']) 
    nR = len(df03R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df03R['resposta'][j])
    st.write('EQUIPE 04:')    
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df04R['resposta'])
    nR = len(df04R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df04R['resposta'][j])
    st.write('EQUIPE 05:')    
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df05R['resposta'])  
    nR = len(df05R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df05R['resposta'][j])
    st.write('EQUIPE 06:')    
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df06R['resposta'])
    nR = len(df06R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df06R['resposta'][j])
    st.write('EQUIPE 07:')    
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df07R['resposta'])
    nR = len(df07R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df07R['resposta'][j])
    st.write('EQUIPE 08:')    
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df08R['resposta'])  
    nR = len(df08R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df08R['resposta'][j])
    st.write('EQUIPE 09:')    
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df09R['resposta']) 
    nR = len(df09R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df09R['resposta'][j])
    st.write('EQUIPE 10:')    
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df10R['resposta']) 
    nR = len(df10R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df10R['resposta'][j])
    st.write('EQUIPE 11:')      
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df11R['resposta']) 
    nR = len(df11R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df11R['resposta'][j])
    st.write('EQUIPE 12:')      
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df12R['resposta'])  
    nR = len(df12R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df12R['resposta'][j])
    st.write('EQUIPE 13:')    
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df13R['resposta'])  
    nR = len(df13R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df13R['resposta'][j])
    st.write('EQUIPE 14:')      
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df14R['resposta'])  
    nR = len(df14R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df14R['resposta'][j])
    st.write('EQUIPE 15:')      
    st.info('Resposta do(a) TUTOR(A):')
    #st.write(df15R['resposta'])
    nR = len(df15R['resposta'])
    for j in range(nR):
      with st.chat_message("user", avatar = "👨‍⚖️"):
        st.write(df15R['resposta'][j])
elif choice == "Dúvidas e Respostas":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    colDR1, colDR2 = st.columns((1,1))
    with colDR1:
        st.write("Nº TOTAL de Dúvidas (Todas as Equipes):")
        st.warning(NregD)
    with colDR2:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregR)
    st.sidebar.info("Índicador de Eficiência = " + str(100*NregR/NregD)+"%")
    #EQUIPE 01
    st.subheader('EQUIPE 01:')
    colD1, colR1 = st.columns((1,1))
    with colD1:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df01D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df01D['duvida'][i]) 
    with colR1:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df01R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df01R['resposta'][j])
    #EQUIPE 02
    st.subheader('EQUIPE 02:')
    colD2, colR2 = st.columns((1,1))
    with colD2:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df02D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df02D['duvida'][i]) 
    with colR2:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df02R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df02R['resposta'][j])
    #EQUIPE 03
    st.subheader('EQUIPE 03:')
    colD3, colR3 = st.columns((1,1))
    with colD3:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df03D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df03D['duvida'][i]) 
    with colR3:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df03R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df03R['resposta'][j])
    #EQUIPE 04
    st.subheader('EQUIPE 04:')
    colD4, colR4 = st.columns((1,1))
    with colD4:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df04D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df04D['duvida'][i]) 
    with colR4:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df04R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df04R['resposta'][j])
    #EQUIPE 05
    st.subheader('EQUIPE 05:')
    colD5, colR5 = st.columns((1,1))
    with colD5:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df05D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df05D['duvida'][i]) 
    with colR5:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df05R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df05R['resposta'][j])
    #EQUIPE 06
    st.subheader('EQUIPE 06:')
    colD6, colR6 = st.columns((1,1))
    with colD6:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df06D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df06D['duvida'][i]) 
    with colR6:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df06R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df06R['resposta'][j])
    #EQUIPE 07
    st.subheader('EQUIPE 07:')
    colD7, colR7 = st.columns((1,1))
    with colD7:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df07D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df07D['duvida'][i]) 
    with colR7:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df07R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df07R['resposta'][j])    
    #EQUIPE 08
    st.subheader('EQUIPE 08:')
    colD8, colR8 = st.columns((1,1))
    with colD8:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df08D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df08D['duvida'][i]) 
    with colR8:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df08R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df08R['resposta'][j])
    #EQUIPE 09
    st.subheader('EQUIPE 09:')
    colD9, colR9 = st.columns((1,1))
    with colD9:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df09D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df09D['duvida'][i]) 
    with colR9:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df09R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df09R['resposta'][j])
    #EQUIPE 10
    st.subheader('EQUIPE 10:')
    colD10, colR10 = st.columns((1,1))
    with colD10:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df10D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df10D['duvida'][i]) 
    with colR10:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df10R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df10R['resposta'][j])
    #EQUIPE 11
    st.subheader('EQUIPE 11:')
    colD11, colR11 = st.columns((1,1))
    with colD11:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df11D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df11D['duvida'][i]) 
    with colR11:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df11R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df11R['resposta'][j])
    #EQUIPE 12
    st.subheader('EQUIPE 12:')
    colD12, colR12 = st.columns((1,1))
    with colD12:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df12D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df12D['duvida'][i]) 
    with colR12:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df12R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df12R['resposta'][j])
    
    #EQUIPE 13
    st.subheader('EQUIPE 13:')
    colD13, colR13 = st.columns((1,1))
    with colD13:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df13D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df13D['duvida'][i]) 
    with colR13:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df13R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df13R['resposta'][j])
    #EQUIPE 14
    st.subheader('EQUIPE 14:')
    colD14, colR14 = st.columns((1,1))
    with colD14:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df14D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df14D['duvida'][i]) 
    with colR14:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df14R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df14R['resposta'][j])
    #EQUIPE 15
    st.subheader('EQUIPE 15:')
    colD15, colR15 = st.columns((1,1))
    with colD15:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df15D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df15D['duvida'][i]) 
    with colR15:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df15R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df15R['resposta'][j])
  
elif choice == "EQUIPE 01":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 01:')
    colEQ01D, colEQ01R = st.columns((1,1))
    with colEQ01D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df01D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df01D['duvida'][i]) 
    with colEQ01R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df01R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df01R['resposta'][j])        
elif choice == "EQUIPE 02":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 02:')
    colEQ02D, colEQ02R = st.columns((1,1))
    with colEQ02D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df02D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df02D['duvida'][i]) 
    with colEQ02R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df02R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df02R['resposta'][j])         
elif choice == "EQUIPE 03":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 03:')
    colEQ03D, colEQ03R = st.columns((1,1))
    with colEQ03D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df03D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df03D['duvida'][i]) 
    with colEQ03R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df03R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df03R['resposta'][j])  
elif choice == "EQUIPE 04":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 04:')
    colEQ04D, colEQ04R = st.columns((1,1))
    with colEQ04D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df04D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df04D['duvida'][i]) 
    with colEQ04R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df04R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df04R['resposta'][j])  
elif choice == "EQUIPE 05":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 05:')
    colEQ05D, colEQ05R = st.columns((1,1))
    with colEQ05D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df05D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df05D['duvida'][i]) 
    with colEQ05R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df05R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df05R['resposta'][j])  
elif choice == "EQUIPE 06":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 06:')
    colEQ06D, colEQ06R = st.columns((1,1))
    with colEQ06D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df06D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df06D['duvida'][i]) 
    with colEQ06R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df06R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df06R['resposta'][j])  
elif choice == "EQUIPE 07":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 07:')
    colEQ07D, colEQ07R = st.columns((1,1))
    with colEQ07D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df07D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df07D['duvida'][i]) 
    with colEQ07R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df07R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df07R['resposta'][j])  
elif choice == "EQUIPE 08":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 08:')
    colEQ08D, colEQ08R = st.columns((1,1))
    with colEQ08D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df08D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df08D['duvida'][i]) 
    with colEQ08R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df08R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df08R['resposta'][j])  
elif choice == "EQUIPE 09":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 09:')
    colEQ09D, colEQ09R = st.columns((1,1))
    with colEQ09D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df09D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df09D['duvida'][i]) 
    with colEQ09R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df09R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df09R['resposta'][j])  
elif choice == "EQUIPE 10":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 10:')
    colEQ10D, colEQ10R = st.columns((1,1))
    with colEQ10D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df10D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df10D['duvida'][i]) 
    with colEQ10R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df10R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df10R['resposta'][j])  
elif choice == "EQUIPE 11":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 11:')
    colEQ11D, colEQ11R = st.columns((1,1))
    with colEQ11D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df11D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df11D['duvida'][i]) 
    with colEQ11R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df11R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df11R['resposta'][j])     
elif choice == "EQUIPE 12":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 12:')
    colEQ12D, colEQ12R = st.columns((1,1))
    with colEQ12D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df12D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df12D['duvida'][i]) 
    with colEQ12R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df12R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df12R['resposta'][j]) 
elif choice == "EQUIPE 13":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 13:')
    colEQ13D, colEQ13R = st.columns((1,1))
    with colEQ13D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df13D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df13D['duvida'][i]) 
    with colEQ13R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df13R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df13R['resposta'][j]) 
elif choice == "EQUIPE 14":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 14:')
    colEQ14D, colEQ14R = st.columns((1,1))
    with colEQ14D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df14D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df14D['duvida'][i]) 
    with colEQ14R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df14R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df14R['resposta'][j]) 
elif choice == "EQUIPE 15":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 15:')
    colEQ15D, colEQ15R = st.columns((1,1))
    with colEQ15D:
      st.warning('Dúvida(s) Enviada(s)')
      nD = len(df15D['duvida'])
      for i in range(nD):
        with st.chat_message("user"):   
          st.write(df15D['duvida'][i]) 
    with colEQ15R:        
      st.success('Resposta do(a) TUTOR(A):')
      nR = len(df15R['resposta'])
      for j in range(nR):
        with st.chat_message("user", avatar = "👨‍⚖️"):
          st.write(df15R['resposta'][j]) 
elif choice == "Pontos Equipes":
  vetNOTAS = []
  colNotas1, colNotas2 = st.columns((1,1))
  with colNotas1:
    for i in range(n):
      pa = float(dfresumo['Participacao'][i])/qtdDadosPorEquipe[i]
      cr = float(dfresumo['Criatividade'][i])/qtdDadosPorEquipe[i]
      co = float(dfresumo['Coerencia'][i])/qtdDadosPorEquipe[i]
      ap = float(dfresumo['Apresentacao'][i])/qtdDadosPorEquipe[i]
      mvp =  float(dfresumo['MVP'][i])/qtdDadosPorEquipe[i]
      inov = float(dfresumo['Inovacao'][i])/qtdDadosPorEquipe[i]
      nota = pa + cr + co + ap + mvp + inov
      vetNOTAS.append(nota)
      st.subheader("Média Total da " + str(rotulo[i]))
      st.subheader(nota)
      st.write('')
  with colNotas2:
    DF = pd.DataFrame(vetNOTAS)
    DF.columns = ['Notas']
    DF.index = rotulo
    st.dataframe(DF.sort_values(by='Notas', ascending=False))
 fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 270,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Speed"}))
fig.show()
