import pandas as pd
import streamlit as st
import plotly.graph_objs as go


st.set_page_config(page_title="Estimación del rezago habitacional utilizando imágenes satelitales", page_icon=":house:")




st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 35px; text-align: center'>Estimación del rezago habitacional utilizando imágenes satelitales</p>", unsafe_allow_html=True)
st.image("https://centrourbano.com/revista/wp-content/uploads/Dia-Nacional-de-la-Vivienda-se-reduce-el-rezago-habitacional-en-Mexico-1280x720.jpg", width=700)
st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 20px; text-align: center'>¿Qué es el rezago habitacional?</p>", unsafe_allow_html=True)

#Añadir mapa de folium

st.write("El rezago habitacional es la diferencia entre la vivienda que se necesita y la que se tiene. Se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la ")

st.markdown("<p style='font-family: Montserrat; font-weight: bold;font-size: 20px; text-align: center'>¿Cómo se mide el rezago habitacional?</p>", unsafe_allow_html=True)
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
