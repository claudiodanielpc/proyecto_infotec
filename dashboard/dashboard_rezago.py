import pandas as pd
import streamlit as st
import plotly.graph_objs as go
import polars as pl
from streamlit_extras.dataframe_explorer import dataframe_explorer
#from streamlit_pandas_profiling import st_profile_report
from streamlit.elements import spinner




st.set_page_config(page_title="Estimación del rezago habitacional utilizando imágenes satelitales", page_icon=":house:")




st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 35px; text-align: center'>Estimación del rezago habitacional utilizando imágenes satelitales</p>", unsafe_allow_html=True)
st.image("https://centrourbano.com/revista/wp-content/uploads/Dia-Nacional-de-la-Vivienda-se-reduce-el-rezago-habitacional-en-Mexico-1280x720.jpg", width=700)
st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 20px; text-align: center'>¿Qué es el rezago habitacional?</p>", unsafe_allow_html=True)

#Añadir mapa de folium
st.markdown("<p style='font-family: Montserrat; font-size: 15px; text-align: justified'>El rezago habitacional es una metodología desarrollada por la Comisión Nacional de Vivienda, la cual está basada en los tipos de materiales utilizados para la construcción y de los espacios que los habitantes de éstas ocupan.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 20px; text-align: center'>¿Cómo se mide el rezago habitacional?</p>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Para la cuantificación del rezago, se consideran las siguientes variables y condiciones:</p>", unsafe_allow_html=True)
st.image("https://github.com/claudiodanielpc/proyecto_infotec/raw/main/rezago.png", width=700)


#Añadir sidebar
st.sidebar.markdown("<p style='font-family: Montserrat; font-weight: bold;'>Menú</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-family: Montserrat;'>¿Quiéres saber más?</p>", unsafe_allow_html=True)

#Añadir opciones
option = st.sidebar.selectbox(
    'Selecciona una opción',
        ['Sobre el proyecto', 'Fuentes de información']) #Formato de la fuente   

if option == 'Sobre el proyecto':
    st.sidebar.write("El proyecto tiene como objetivo proporcionar una forma alternativa de medición del rezago habitacional utilizando imágenes satelitales.")
    st.sidebar.write("La idea no solo es xxx")

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

#Base de datos
st.markdown("---")
st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 20px; text-align: center'>Sobre la base de datos</p>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>El rezago habitacional se calcula utilizando la Encuesta Nacional de Ingresos y Gastos de los Hogares y se puede utilizar la muestra del cuestionario ampliado del Censo para obtener resultados a nivel municipal.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>No obstante se utilizará la información a nivel manzana para aproximar una medición similar de carencias. La información de viviendas se transformó a porcentajes para poder comparar.</p>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Estructura de la base limpia: </p>", unsafe_allow_html=True)

#Leer base de datos
df = pl.read_csv("https://gitlab.com/claudiodanielpc/infotec/-/raw/main/df_limpia.csv")

row_count = "{:,}".format(df.shape[0])
col_count = "{:,}".format(df.shape[1])
st.markdown(f"<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>La base de datos tiene las siguientes características</p>", unsafe_allow_html=True)
st.markdown(f"<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Observaciones: {row_count}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Variables: {col_count}</p>", unsafe_allow_html=True)
#Tabla con 10 registros

st.dataframe(df.head(10).to_pandas())

#Filtro por variable para obtener estadísticas descriptivas pandas pro
st.markdown("---")
st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 20px; text-align: center'>Estadísticas descriptivas de la base limpia</p>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Selecciona una variable para obtener sus estadísticas descriptivas</p>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Recuerda que la tabla puede tardar un poco debido a la cantidad de información a procesar. Te pedimos paciencia 😊</p>", unsafe_allow_html=True)
#Filtro por variable
variable = st.selectbox(
    'Selecciona una variable',
    df.columns)

st.markdown(f"<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Estadísticas descriptivas de la variable {variable}</p>", unsafe_allow_html=True)
st.dataframe(df[variable].describe().to_pandas())


#Mapa
st.header("Mapa de rezago habitacional")

#mapa en blanco de México con plotly

data=go.Scattergeo(
    lat = [23.6345],
    lon = [-102.5528],
    mode = 'markers',
    marker_color = 'rgba(255, 0, 0, .8)',
    marker_size = 10,
    text = ["México"],
    hoverinfo = 'text'
)

layout = go.Layout(
    title = go.layout.Title(
        text = 'Mapa de rezago habitacional en México'
    ),
    geo = go.layout.Geo(
        scope = 'north america',
        projection_type = 'azimuthal equal area',
        showland = True,
        landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
        lonaxis_range= [-125, -85],
        lataxis_range= [5, 35]
    ),
)

fig = go.Figure(data=data, layout=layout)

st.plotly_chart(fig)

st.markdown("---")

left_info_col, right_info_col = st.columns(2)

left_info_col.markdown(
        f"""
        ### Autor
        Comentarios, preguntas o sugerencias.
        ##### Claudio Daniel Pacheco-Castro [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/bukotsunikki.svg?style=social&label=Follow%20%40claudiodanielpc)](https://twitter.com/claudiodanielpc)
        - Email:  <claudio@comunidad.unam.mx> o <claudiodanielpc@gmail.com>
        - GitHub: https://github.com/claudiodanielpc
        """,
        unsafe_allow_html=True,
    )


