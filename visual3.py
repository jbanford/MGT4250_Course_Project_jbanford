import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
import pandas as pd
st.title("Visualizations III")
df1 = pd.read_excel("MGT4250 Course Project Data.xlsx",sheet_name='Sheet2')
df2 = df1.melt(id_vars=['Year'], value_name='Genre')
df_clean = df2.drop(columns=['variable'])
col1, col2 = st.columns([0.5, 0.5])
with col1:
    st.dataframe(df_clean)
with col2:
    grouped = df_clean.groupby(['Year', 'Genre']).size().reset_index(name='Count')
    st.dataframe(grouped)
selected_year = st.selectbox("Select Year", grouped["Year"].unique())
year_subset = grouped[grouped['Year'] == selected_year]
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.pie(year_subset['Count'], labels=year_subset['Genre'], autopct='%1.1f%%', startangle=140)
plt.title(f"Genre Proportions for Year {selected_year}")
plt.axis('equal')
st.pyplot()

grouped2 = df_clean.groupby(['Genre']).size().reset_index(name='Count')
plt.figure(figsize=(8, 6))
plt.pie(grouped2['Count'], labels=grouped2['Genre'], autopct='%1.1f%%', startangle=140)
plt.title(f"Genre Proportions for 2012-2022")
plt.axis('equal')
st.pyplot()

