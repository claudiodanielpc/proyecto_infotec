import pandas as pd
import streamlit as st
import plotly.graph_objs as go

st.set_page_config(page_title="Estimación del rezago habitacional utilizando imágenes satelitales", page_icon=":house:")

st.title("Estimación del rezago habitacional utilizando imágenes satelitales")
st.image("https://centrourbano.com/revista/wp-content/uploads/Dia-Nacional-de-la-Vivienda-se-reduce-el-rezago-habitacional-en-Mexico-1280x720.jpg", width=700)
st.header("¿Qué es el rezago habitacional?")
#Añadir mapa de folium

st.write("El rezago habitacional es la diferencia entre la vivienda que se necesita y la que se tiene. Se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la ")

st.header("¿Cómo se mide el rezago habitacional?")
st.image("https://github.com/claudiodanielpc/proyecto_infotec/raw/main/rezago.png", width=700)

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
