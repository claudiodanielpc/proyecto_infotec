import streamlit as st
import pandas as pd
import polars as pl
import plotly.graph_objs as go
import plotly.express as px

@st.cache_data
def load_data():
    """
    Load cleaned data from remote CSV file and return as Pandas DataFrame
    """
    #url = "https://gitlab.com/claudiodanielpc/infotec/-/raw/main/df_limpia.csv"
    df = pl.read_csv('https://gitlab.com/claudiodanielpc/infotec/-/raw/main/final1.csv')
    #df = pl.read_csv("https://gitlab.com/claudiodanielpc/infotec/-/raw/main/df_limpia.csv")
    return df


def show_data_info(df):
    """
    Display basic information about the loaded DataFrame
    """
    row_count = "{:,}".format(df.shape[0])
    col_count = "{:,}".format(df.shape[1])
    st.markdown(f"<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>La base de datos tiene las siguientes características</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Observaciones: {row_count}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Variables: {col_count}</p>", unsafe_allow_html=True)

def show_data_preview(df):
    """
    Display a preview of the loaded DataFrame
    """
    st.dataframe(df.head(10).to_pandas())


def show_variable_stats(df):
    """
    Display descriptive statistics for a selected variable from the loaded DataFrame
    """
    variable = st.selectbox(
        'Selecciona una variable',
        df.columns)
    st.markdown(f"<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Estadísticas descriptivas de la variable {variable}</p>", unsafe_allow_html=True)
    st.dataframe(df[variable].describe())

def hist_plotly(df):
    """
    Mostrar el histograma de acuerdo con el nom_ent seleccionado
    """
    nom_ent = st.selectbox(
        'Selecciona una entidad',
        df['nom_ent'].unique())
    #generar una subtabla con la entidad seleccionada
    filtro=df.filter(df['nom_ent'] == nom_ent)
    st.markdown(f"<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Histograma del índice de rezago habitacional de {nom_ent}</p>", unsafe_allow_html=True)
    fig = px.histogram(filtro, x=filtro["ind_rez"], nbins=10, color_discrete_sequence=['#F63366'])
    fig.update_layout(
    xaxis_title='Índice de rezago habitacional',
    yaxis_title='Número de manzanas',
    font_family='Montserrat',
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

#     fig.update_layout(
#     xaxis_title='Índice de rezago habitacional',
#     yaxis_title='Número de manzanas',
#     font_family='Montserrat',
#     annotations=[
#         go.layout.Annotation(
#             text='Fuente: INEGI. Encuesta Nacional de Ingresos y Gastos de los Hogares (ENIGH) 2020',
#             xref='paper',
#             yref='paper',
#             x=0,
#             y=-0.2,
#             showarrow=False,
#             font=dict(
#                 family='Montserrat',
#                 size=12,
#                 color='grey'
#             )
#         )
#     ]
# )
