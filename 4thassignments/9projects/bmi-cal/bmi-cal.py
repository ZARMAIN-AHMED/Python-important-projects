import streamlit as st
import pandas as pandas

st.title("BMI CALCULATOR")

height = st.slider("Enter Your height (in cm):", 100, 250, 175)
weight =st.slider("Enter Your weight (in kg)" , 40 , 200 , 70)


bmi = weight / ((height/100) ** 2)
st.write(f"Your BMI is {bmi: .2f}")
st.write("### BMI Categories ###")
st.write("- Underweight : BMI less than 18.5")
st.write("- Normal weight : BMI between 18.5 and 24.9")
st. write ("- Overweight :BMI between 25 an 29.9")
st.write("- Obesity: BMI 30 or greater")



# !pip install streamlit
# !pip install pyngrok

# from google.colab import userdata
# pyngrok_authtoken = userdata.get('pyngrok-token')

# !ngrok authtoken 2tiyYCsv9D9nA8yj03aoR9s7Y1j_2ZAALCWKS6ybRT2t5s2Y7


# from pyngrok import ngrok

# !streamlit run app.py &>/ dev/null &
# public_url = ngrok. connect(addr=8501)
# public_url