from shiny import App, Inputs, Outputs, Session, reactive, render, ui
import folium
import pandas as pd


app_ui = ui.page_fluid(
    ui.h1("Estimación del rezago habitacional utilizando imágenes satelitales",
          style="font-family: 'Montserrat'; font-size: 30px; font-weight: 700; color: #000000; text-align: center;"),
          #Añadir imagen
    ui.img(src="https://centrourbano.com/revista/wp-content/uploads/Dia-Nacional-de-la-Vivienda-se-reduce-el-rezago-habitacional-en-Mexico-1280x720.jpg", width="100%", height="100%"),
    #Texto
    ui.h2("¿Qué es el rezago habitacional?", style="font-family: 'Montserrat'; font-size: 20px; font-weight: 700; color: #000000; text-align: center;"),
    #Explicación del rezago habitacional
    ui.p("El rezago habitacional es la diferencia entre la vivienda que se necesita y la que se tiene. Se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la calidad de la vivienda, el acceso a servicios básicos y la seguridad de la vivienda. El rezago habitacional se mide en términos de la "),

ui.div(
    ui.h2("¿Cómo se mide el rezago habitacional?", style="font-family: 'Montserrat'; font-size: 20px; font-weight: 700; color: #000000; text-align: center;"),
    ui.img(src="https://github.com/claudiodanielpc/proyecto_infotec/raw/main/rezago.png", width="100%", height="100%"),

    ui.h2("Mapa de rezago habitacional", style="font-family: 'Montserrat'; font-size: 20px; font-weight: 700; color: #000000; text-align: center;"),
    ui.div(id="map", style="height: 500px; width: 100%;")
)
)
#Mapa



#server
def server(input, output, session):
    pass

app = App(ui=app_ui, server=server)