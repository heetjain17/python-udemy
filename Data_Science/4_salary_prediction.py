import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

data = pd.read_csv("experience_salary.csv")

x = data[["YearsExperience"]]
y = data[["Salary"]]

model = LinearRegression()
model.fit(x, y)

st.title("Salary Predictor Based on Experience")
st.write("Enter your years of experience to predict your salary:")

col1, col2 = st.columns(2)

with col1:
  years_input = st.number_input("Years of experience", min_value=0.0, max_value=50.0, step=1.0)

st.caption("This prediction is based on a simple linear regression model trained on past experience-salary data.")

if years_input is not None:
  predicted_salary = model.predict(pd.DataFrame([[years_input]], columns=["YearsExperience"]))[0]
  st.success(f"Estimated Salary: ₹{predicted_salary[0]:,.2f}")

st.subheader("Regression Line")

fig, ax = plt.subplots()
ax.scatter(x, y, color="#1f77b4", label="Actual Data")
ax.plot(x, model.predict(x), color="#ff5733", linewidth=2, label="Regression Line")

ax.set_xlabel("Years of Experience")
ax.set_ylabel("Salary")
ax.set_title("Salary vs Experience")
ax.legend()
ax.grid(True)
st.pyplot(fig)