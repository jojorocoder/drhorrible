import pandas as pd
import plotly.express as px
import streamlit as st
import os


df = pd.read_csv('vehicles_us.csv')

# Streamlit header
st.header('Car Sales Data Visualization')

# Checkbox display
show_histogram = st.checkbox('Show Histogram', value=True)
show_scatterplot = st.checkbox('Show Scatter Plot', value=True)

# Display Histogram if checkbox is checked
if show_histogram:
    st.subheader('Price Distribution by Car Condition')
    fig_hist= px.histogram(df, x='price', color='condition', nbins=50, title='Price Distribution by Car Condition', opacity=0.7, barmode='overlay')
    st.plotly_chart(fig_hist)


# Display Scatter Plot if checkbox is checked
if show_scatterplot:
    st.subheader('Price of Car Type based of Mileage')
    fig_scatter= px.scatter(df, x='odometer', y='price', color='type', title='Price vs. Odometer of Car Type')
    st.plotly_chart(fig_scatter)
