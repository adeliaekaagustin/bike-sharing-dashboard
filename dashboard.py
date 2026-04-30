import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Dashboard Bike Sharing")

df = pd.read_csv("main_data.csv")

df['season'] = df['season'].map({
    1:'Spring',2:'Summer',3:'Fall',4:'Winter'
})

df['weathersit'] = df['weathersit'].map({
    1:'Clear',2:'Mist',3:'Light Snow',4:'Heavy Rain'
})

st.sidebar.title("Filter")

season = st.sidebar.selectbox(
    "Pilih Musim",
    df['season'].unique()
)

filtered_df = df[df['season'] == season]

st.subheader("Rata-rata Peminjaman")
st.write(filtered_df['cnt'].mean())

st.subheader("Cuaca vs Peminjaman")
fig, ax = plt.subplots()
sns.barplot(data=filtered_df, x='weathersit', y='cnt', ax=ax)
st.pyplot(fig)

st.subheader("Temperatur vs Peminjaman")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_df, x='temp', y='cnt', ax=ax2)
st.pyplot(fig2)

st.subheader("Hari Kerja vs Weekend")
fig3, ax3 = plt.subplots()
sns.barplot(data=filtered_df, x='workingday', y='cnt', ax=ax3)
st.pyplot(fig3)

st.write("Insight: Cuaca cerah dan temperatur hangat meningkatkan peminjaman.")