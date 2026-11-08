import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
def load_data(file):
   return pd.read_csv(file)

   
file = st.file_uploader("Upload file", type=["csv"])
if file is not None:
    df = load_data (file)
    st.write(df)
    n_rows = st.slider("Number of rows to display", min_value=5, max_value=len(df), step=1)
    columns_to_show = st.multiselect("Select columns to display", df.columns, default=df.columns.tolist())
    st.write(df.head(n_rows)[columns_to_show])
    tab1,tab2=st.tabs(["Scatter Plot","Histogram"])
    with tab1:
     col1,col2,col3=st.columns(3)
    with col1:
        x_column = st.selectbox("Select x-axis column", df.columns)
    with col2:
        y_column = st.selectbox("Select y-axis column", df.columns)
    with col3:
     color = st.selectbox("select column to be color ",df.columns)
     fig_scatter = px.scatter(df, x=x_column, y=y_column , color=color)
    st.plotly_chart(fig_scatter)
    with tab2:
        histogram_feature = st.selectbox("Select feature for histogram", df.columns)
        fig_hist = px.histogram(df, x=histogram_feature, color=color)
        st.plotly_chart(fig_hist)