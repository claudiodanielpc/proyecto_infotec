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
    st.markdown(f"<p style='font-family: Montserrat;font-size: 15px; text-align: justified'>Histograma de la variable {nom_ent}</p>", unsafe_allow_html=True)
    fig = px.histogram(filtro, x=df["ind_rez"], nbins=10, color_discrete_sequence=['#F63366'])
    #fig = px.histogram(filtro.filter(filtro['nom_ent'] == nom_ent), x=df["ind_rez"], nbins=10, color_discrete_sequence=['#F63366'])
    st.plotly_chart(fig)