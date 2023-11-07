#libraries
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#from urllib.error import URLError

#DÚVIDAS
rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vRzPHn3E7ZBSxmVq5lKH5GYxtu0IykxSkWCS16RHYmyXXHmvlErzXF7EJhetiZysvF3i5QP5r8Ti2nY/pub?gid=1211657281&single=true&output=csv')
dataD = rD.content
dfD = pd.read_csv(BytesIO(dataD), index_col=0)
NregD = len(dfD)
dfD.columns = ['equipe', 'nome', 'duvida', 'obs']

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
stopwords.update(["de", "ao", "o", "nao", "para", "da", "meu", "em", "você", "ter", "um", "ou", "os", "ser", "só"])
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
    st.code(df01D['duvida']) 
    st.write('EQUIPE 02:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df02D['duvida']) 
    st.write('EQUIPE 03:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df03D['duvida']) 
    st.write('EQUIPE 04:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df04D['duvida']) 
    st.write('EQUIPE 05:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df05D['duvida']) 
    st.write('EQUIPE 06:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df06D['duvida'])
    st.write('EQUIPE 07:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df07D['duvida']) 
    st.write('EQUIPE 08:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df08D['duvida']) 
    st.write('EQUIPE 09:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df09D['duvida']) 
    st.write('EQUIPE 10:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df10D['duvida']) 
    st.write('EQUIPE 11:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df11D['duvida']) 
    st.write('EQUIPE 12:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df12D['duvida']) 
    st.write('EQUIPE 13:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df13D['duvida']) 
    st.write('EQUIPE 14:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df14D['duvida'])
    st.write('EQUIPE 15:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df15D['duvida'])  
    st.subheader("HISTÓRICO DE DÚVIDAS: ")
    st.code(dfD['equipe'] + ":" + dfD['duvida'])
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
elif choice == "Respostas":       
    st.header("Painel Analítico: RESPOSTAS")    
    st.write('EQUIPE 01:')    
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df01R['resposta'])  
    st.write('EQUIPE 02:')    
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df02R['resposta'])  
    st.write('EQUIPE 03:')    
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df03R['resposta'])  
    st.write('EQUIPE 04:')    
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df04R['resposta'])      
    st.write('EQUIPE 05:')    
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df05R['resposta'])  
    st.write('EQUIPE 06:')    
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df06R['resposta'])  
    st.write('EQUIPE 07:')    
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df07R['resposta'])  
    st.write('EQUIPE 08:')    
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df08R['resposta'])  
    st.write('EQUIPE 09:')    
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df09R['resposta'])  
    st.write('EQUIPE 10:')    
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df10R['resposta'])  
    st.write('EQUIPE 11:')      
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df11R['resposta'])  
    st.write('EQUIPE 12:')      
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df12R['resposta'])  
    st.write('EQUIPE 13:')    
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df13R['resposta'])  
    st.write('EQUIPE 14:')      
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df14R['resposta'])  
    st.write('EQUIPE 15:')      
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df15R['resposta'])                 
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
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df01D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df01R['resposta'])  
    #EQUIPE 02
    st.subheader('EQUIPE 02:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df02D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df02R['resposta'])     
    #EQUIPE 03
    st.subheader('EQUIPE 03:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df03D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df03R['resposta']) 
    #EQUIPE 04
    st.subheader('EQUIPE 04:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df04D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df04R['resposta']) 
    #EQUIPE 05
    st.subheader('EQUIPE 05:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df05D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df05R['resposta'])    
    #EQUIPE 06
    st.subheader('EQUIPE 06:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df06D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df06R['resposta'])  
    #EQUIPE 07
    st.subheader('EQUIPE 07:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df07D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df07R['resposta'])     
    #EQUIPE 08
    st.subheader('EQUIPE 08:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df08D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df08R['resposta']) 
    #EQUIPE 09
    st.subheader('EQUIPE 09:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df09D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df09R['resposta']) 
    #EQUIPE 10
    st.subheader('EQUIPE 10:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df10D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df10R['resposta']) 
    #EQUIPE 11
    st.subheader('EQUIPE 11:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df11D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df11R['resposta']) 
    #EQUIPE 12
    st.subheader('EQUIPE 12:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df12D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df12R['resposta']) 
    
    #EQUIPE 13
    st.subheader('EQUIPE 13:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df13D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df13R['resposta']) 
    #EQUIPE 14
    st.subheader('EQUIPE 14:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df14D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df14R['resposta']) 
    #EQUIPE 15
    st.subheader('EQUIPE 15:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df15D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df15R['resposta']) 
  
elif choice == "EQUIPE 01":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 01:')
    colEQ11, colEQ12 = st.columns((1,1))
    with colEQ11:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf01D)
    with colEQ12:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf01R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df01D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df01R['resposta'])   
        
elif choice == "EQUIPE 02":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 02:')
    colEQ21, colEQ22 = st.columns((1,1))
    with colEQ21:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf02D)
    with colEQ22:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf02R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df02D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df02R['resposta'])    
        
elif choice == "EQUIPE 03":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 03:')
    colEQ31, colEQ32 = st.columns((1,1))
    with colEQ31:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf03D)
    with colEQ32:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf03R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df03D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df03R['resposta'])  
        
elif choice == "EQUIPE 04":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 04:')
    colEQ41, colEQ42 = st.columns((1,1))
    with colEQ41:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf04D)
    with colEQ42:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf04R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df04D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df04R['resposta'])  
        
elif choice == "EQUIPE 05":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 05:')
    colEQ51, colEQ52 = st.columns((1,1))
    with colEQ51:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf05D)
    with colEQ52:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf05R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df05D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df05R['resposta'])        

elif choice == "EQUIPE 06":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 06:')
    colEQ61, colEQ62 = st.columns((1,1))
    with colEQ61:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf06D)
    with colEQ62:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf06R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df06D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df06R['resposta'])   
        
elif choice == "EQUIPE 07":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 07:')
    colEQ71, colEQ72 = st.columns((1,1))
    with colEQ71:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf07D)
    with colEQ72:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf07R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df07D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df07R['resposta'])    
        
elif choice == "EQUIPE 08":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 08:')
    colEQ81, colEQ82 = st.columns((1,1))
    with colEQ81:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf08D)
    with colEQ82:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf08R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df08D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df08R['resposta'])  
        
elif choice == "EQUIPE 09":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 09:')
    colEQ91, colEQ92 = st.columns((1,1))
    with colEQ91:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf09D)
    with colEQ92:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf09R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df09D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df09R['resposta'])  
        
elif choice == "EQUIPE 10":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 10:')
    colEQ101, colEQ102 = st.columns((1,1))
    with colEQ101:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf10D)
    with colEQ102:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf10R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df10D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df10R['resposta']) 
        
elif choice == "EQUIPE 11":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 11:')
    colEQ111, colEQ112 = st.columns((1,1))
    with colEQ111:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf11D)
    with colEQ112:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf11R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df11D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df11R['resposta']) 
    
elif choice == "EQUIPE 12":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 12:')
    colEQ111, colEQ112 = st.columns((1,1))
    with colEQ111:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf11D)
    with colEQ112:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf11R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df12D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df12R['resposta'])   

elif choice == "EQUIPE 13":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 13:')
    colEQ111, colEQ112 = st.columns((1,1))
    with colEQ111:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf13D)
    with colEQ112:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf13R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df13D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df13R['resposta'])  
  
elif choice == "EQUIPE 14":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 14:')
    colEQ111, colEQ112 = st.columns((1,1))
    with colEQ111:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf14D)
    with colEQ112:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf14R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df14D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df14R['resposta']) 

elif choice == "EQUIPE 15":       
    st.header("Painel Analítico: DÚVIDAS E RESPOSTAS")  
    st.subheader('EQUIPE 15:')
    colEQ111, colEQ112 = st.columns((1,1))
    with colEQ111:
        st.write("Nº TOTAL de Dúvidas:")
        st.warning(NregDf15D)
    with colEQ112:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf15R)
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df15D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df15R['resposta'])   
