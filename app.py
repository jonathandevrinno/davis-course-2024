import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

data = pd.read_csv("tips.csv")

st.subheader("Tugas Davis")

plt.scatter(data['day'], data['tip'])
st.write("Scatter Plot")
plt.xlabel('Day')
plt.ylabel('Tip')
st.pyplot(plt)

st.write("Line Plot")
fig, ax = plt.subplots(figsize=(10, 6))
line_plot = sns.lineplot(data=data.drop(['total_bill'], axis=1), ax=ax)
st.pyplot(fig)

st.write(f'Nama : Jonathan Devrinno')
st.write(f'NPM : 21082010204')
