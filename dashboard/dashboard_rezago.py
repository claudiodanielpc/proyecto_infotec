import pandas as pd
import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import polars as pl
from streamlit_extras.dataframe_explorer import dataframe_explorer
#from streamlit_pandas_profiling import st_profile_report
from streamlit.elements import spinner
import database
import requests
from IPython.display import IFrame






st.set_page_config(page_title="Estimación del rezago habitacional utilizando imágenes satelitales", page_icon=":house:")




st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 35px; text-align: center'>Estimación del rezago habitacional utilizando imágenes satelitales</p>", unsafe_allow_html=True)
st.image("https://centrourbano.com/revista/wp-content/uploads/Dia-Nacional-de-la-Vivienda-se-reduce-el-rezago-habitacional-en-Mexico-1280x720.jpg", width=700)
st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 20px; text-align: center'>¿Qué es el rezago habitacional?</p>", unsafe_allow_html=True)

#Añadir mapa de folium
st.markdown("<p style='font-family: Montserrat; font-size: 15px; text-align: justified'>El rezago habitacional es una metodología desarrollada por la Comisión Nacional de Vivienda, la cual está basada en los tipos de materiales utilizados para la construcción y de los espacios que los habitantes de éstas ocupan.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 20px; text-align: center'>¿Cómo se mide el rezago habitacional?</p>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Para la cuantificación del rezago, se consideran las siguientes variables y condiciones:</p>", unsafe_allow_html=True)
st.image("https://github.com/claudiodanielpc/proyecto_infotec/raw/main/rezago.png", width=700)

#Mostrar código para el cálculo del rezago habitacional
@st.cache_data
def retrieve_code(url):
    response = requests.get(url)
    return response.text

def show_code():
    url_codigo="https://raw.githubusercontent.com/claudiodanielpc/proyecto_infotec/main/dashboard/rezago.r"
    codigo = retrieve_code(url_codigo)
    with st.expander("Mostrar código de cálculo del rezago habitacional con la ENIGH",expanded=False):
        st.code(codigo, language="r")

show_code()



#Añadir sidebar
st.sidebar.markdown("<p style='font-family: Montserrat; font-weight: bold;'>Menú</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-family: Montserrat;'>¿Quiéres saber más?</p>", unsafe_allow_html=True)

#Añadir opciones
option = st.sidebar.selectbox(
    'Selecciona una opción',
        ['Sobre el proyecto', 'Fuentes de información', "Sobre el preprocesamiento"]) #Formato de la fuente   

if option == 'Sobre el proyecto':
    st.sidebar.write("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>El proyecto de investigación propuesto busca, por un lado, proponer una medición alternativa que no dependa del trabajo de campo y levantamiento de un instrumento estadístico como la Encuesta Nacional de Ingresos y Gastos de los Hogares (ENIGH). Por otro lado, mediante su abordaje, se persigue que, igualmente, el análisis del rezago habitacional pueda alcanzar un mayor nivel de desagregación geográfica.</p>", unsafe_allow_html=True)
    st.sidebar.write("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Por otro lado, mediante su abordaje, se persigue que, igualmente, el análisis del rezago habitacional pueda alcanzar un mayor nivel de desagregación geográfica.</p>", unsafe_allow_html=True)
if option== 'Fuentes de información':
    st.sidebar.write("<p style='font-family: Montserrat;'>Las fuentes de información utilizadas para este proyecto son:</p>", unsafe_allow_html=True)
    #ENIGH
    url = "https://www.inegi.org.mx/img/programas/enchogares/ENIGH_ch.gif"
    caption = "INEGI. Encuesta Nacional de Ingresos y Gastos de los Hogares"


    st.sidebar.markdown(
    f"<div style='text-align:center;font-family:montserrat;'>"
    f"<img src='{url}' alt='{caption}' width='70'/>"
    #Añadir url para redirigir a la página del INEGI
    f"<p><a href='https://www.inegi.org.mx/programas/enigh/nc/2020/'>INEGI. Encuesta Nacional de Ingresos y Gastos de los Hogares</a></p>"
    f"</div>",
    unsafe_allow_html=True)



    #Espacio
    st.sidebar.write(" ")
    url = "https://www.inegi.org.mx/img/programas/cpv/cpv2020.png"
    caption = "INEGI. Censo de Población y Vivienda 2020"
#Censo
    st.sidebar.markdown(
    f"<div style='text-align:center; font-family:montserrat;'>"
    f"<img src='{url}' alt='{caption}' width='70'/>"
    #Añadir url para redirigir a la página del INEGI
    f"<p><a href='https://www.inegi.org.mx/programas/ccpv/2020/'>INEGI. Censo de Población y Vivienda 2020</a></p>"
    f"</div>",
    unsafe_allow_html=True)
#Google Earth Engine
    st.sidebar.write(" ")
    url="https://earthengine.google.com/static/images/GoogleEarthEngine_Grey_108.png"
    caption="Google Earth Engine"
    st.sidebar.markdown(
    f"<div style='text-align:center; font-family:montserrat;'>"
    f"<img src='{url}' alt='{caption}' width='70'/>"
    #Añadir url para redirigir a la página del INEGI
    f"<p><a href='https://earthengine.google.com/'>Google Earth Engine</a></p>"
    f"</div>",
    unsafe_allow_html=True)

if option == 'Sobre el preprocesamiento':
    st.sidebar.write("<p style='font-family: Montserrat;'>Los códigos se pueden consultar en:</p>", unsafe_allow_html=True)
    st.sidebar.write(" ")
    url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/600px-Octicons-mark-github.svg.png?20180806170715"
    caption="Preprocesamiento de datos de cuestionario ampliado del Censo 2020"
    st.sidebar.markdown(
    f"<div style='text-align:center; font-family:montserrat;'>"
    f"<img src='{url}' alt='{caption}' width='70'/>"
    #Añadir url para redirigir a la página del INEGI
    f"<p><a href='https://github.com/claudiodanielpc/proyecto_infotec/blob/main/preproc_info_inegi.ipynb'>Preprocesamiento INEGI</a></p>"
    f"</div>",
    unsafe_allow_html=True)


#Mapa
st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 20px; text-align: center'>¿Dónde se concentra el rezago habitacional?</p>", unsafe_allow_html=True)
#Leer datos de rezago
rezago=pd.read_csv("https://raw.githubusercontent.com/claudiodanielpc/proyecto_infotec/main/dashboard/rezago.csv")
fig = px.bar(rezago.sort_values('rezago_vivienda', ascending=True),
                x='rezago_vivienda', y='entidad', orientation='h',color='rezago_vivienda',
                
                color_continuous_scale="YlOrRd")
fig.update_layout(
    coloraxis_colorbar=dict(
        title="% rezago habitacional",
        
        dtick=10
    ))
#Mostrar todos los valores en el eje y
fig.update_layout(yaxis={'tickmode': 'array', 'tickvals': rezago['entidad'], 'ticktext': rezago['entidad']})
fig.update_layout(
    xaxis_title='% de rezago habitacional',
    yaxis_title='Entidad',
    font_family='Montserrat',
     yaxis=dict(
        tickmode='array',
        tickvals=rezago['entidad'],
        ticktext=rezago['entidad'],
        dtick=1
     ),
    annotations=[
        go.layout.Annotation(
            text='Fuente: INEGI. Encuesta Nacional de Ingresos y Gastos de los Hogares (ENIGH) 2020',
            xref='paper',
            yref='paper',
            x=0,
            y=-0.2,
            showarrow=False,
            font=dict(
                family='Montserrat',
                size=12,
                color='grey'
            )
        )
    ]
)
st.plotly_chart(fig)




#Base de datos
st.markdown("---")
st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 20px; text-align: center'>Sobre la base de datos</p>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>El rezago habitacional se calcula utilizando la Encuesta Nacional de Ingresos y Gastos de los Hogares y se puede utilizar la muestra del cuestionario ampliado del Censo para obtener resultados a nivel municipal.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>No obstante se utilizará la información a nivel manzana para aproximar una medición similar de carencias. La información de viviendas se transformó a porcentajes para poder comparar.</p>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Estructura de la base limpia: </p>", unsafe_allow_html=True)
# Cargar datos
df = database.load_data()

# Info básica
database.show_data_info(df)

# Estadística descriptiva de cada variable
database.show_variable_stats(df)

st.markdown("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Si quieres conocer la base de datos completa, puedes descargarla en formato CSV en el siguiente enlace: </p>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'><a href='https://gitlab.com/claudiodanielpc/infotec/-/raw/main/df_limpia.csv'>Liga al archivo CSV</a></p>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 20px; text-align: center'>Sobre las imágenes</p>", unsafe_allow_html=True)
# with st.beta_expander('Show Jupyter Notebook'):
#     notebook_url = 'https://github.com/claudiodanielpc/proyecto_infotec/blob/main/preproc_info_inegi.ipynb'
#     notebook_width = 1000
#     notebook_height = 800
#     iframe(notebook_url, width=notebook_width, height=notebook_height)

# with st.expander('Show Jupyter Notebook'):
#     notebook_url = 'https://gitlab.com/claudiodanielpc/infotec/-/raw/main/preproc_info_inegi.ipynb'
#     notebook_width = 1000
#     notebook_height = 800
#     iframe_code = f'<iframe src="{notebook_url}" width="{notebook_width}" height="{notebook_height}"></iframe>'
#     st.markdown(iframe_code, unsafe_allow_html=True)

# Define the URL of the Jupyter notebook on Binder

# github_url="https://github.com/claudiodanielpc/infotec_prepoc/blob/main/preproc_info_inegi.ipynb"
# #response = requests.get(f"{binder_url}&download=true")
# #response=requests.get(binder_url)
# # html_content = response.content.decode("utf-8")

url="https://nbviewer.org/github/claudiodanielpc/infotec_prepoc/blob/main/preproc_info_inegi.ipynb"
response = requests.get(url)
html_content = response.content.decode("utf-8")

# # # Use the st.components.v1.html() function to embed the HTML content
st.components.v1.html(html_content, height=800, width=800, scrolling=True)

# # Use requests to get the content of the notebook file
# response = requests.get(github_url)
# notebook_content = response.content.decode("utf-8")

# # Define the URL of the notebook on NBViewer
# nbviewer_url = f"https://nbviewer.jupyter.org/url/{github_url.replace('github.com', 'raw.githubusercontent.com')}"
    
# # Use requests to get the HTML version of the notebook from NBViewer
# response = requests.get(f"{nbviewer_url}&raw=true")
# html_content = response.content.decode("utf-8")

# # Use the st.components.v1.html() function to embed the HTML content
# st.components.v1.html(html_content, height=800, width=800)



#Pie de página
st.markdown("---")

left_info_col, right_info_col = st.columns(2)

left_info_col.markdown(
        f"""
        ### Autor
        Comentarios, preguntas o sugerencias.
        ##### Claudio Daniel Pacheco-Castro
        ###### Alumno de la Maestría en Ciencia de Datos e Información. [<img src='https://www.infotec.mx/work/models/Infotec/2019/img/logo_infotec.png' alt='INFOTEC' width='70'/>](https://www.infotec.mx/)
        ###### [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/bukotsunikki.svg?style=social&label=Follow%20%40claudiodanielpc)](https://twitter.com/claudiodanielpc)
        - Email:  <claudio@comunidad.unam.mx> o <claudiodanielpc@gmail.com>
        - GitHub: https://github.com/claudiodanielpc
        """,
        unsafe_allow_html=True,
    )


