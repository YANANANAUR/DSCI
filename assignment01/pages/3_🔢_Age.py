import streamlit as st 

st.title("Age")
st.markdown('Choose your age from 0 to 80')

st.slider("Choose a number from 0 to 80", 0, 80)