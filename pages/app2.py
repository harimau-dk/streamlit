import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit 타이틀 설정
st.title("Viscosity vs Velocity Scatter Plot")

# 데이터 불러오기
df = pd.read_csv("InkjetDB_preprocessing.csv")

# x축과 y축 데이터
x = df["Viscosity"]
y = df["Velocity"]

# Matplotlib로 산점도 그리기
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(x, y, alpha=0.7)
ax.set_title("Viscosity vs Velocity Scatter Plot")
ax.set_xlabel("Viscosity")
ax.set_ylabel("Velocity")
ax.grid(True)

# Streamlit에 그래프 표시
st.pyplot(fig)

st.line_chart(df, x="Viscosity", y="Velocity")
st.scatter_chart(df, x="Viscosity", y="Velocity")