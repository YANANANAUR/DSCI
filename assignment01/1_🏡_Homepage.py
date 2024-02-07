import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image



st.set_page_config(
    page_title="CAN YOU SURVIVE?",
    page_icon="🛳️",
)

st.sidebar.title("Will you SURVIVE?")
st.sidebar.success('select a page above and find out if you can survive')

st.title('Can You survive the Titanic?')
st.markdown('This application will predict whether you will survive in the titanic')

st.header('Intro')
st.write('Explore the depths of history with our Titanic Dashboard Application, an insightful tool born from the Titanic dataset sourced from Kaggles beginner competition. Meticulously crafted by combining gender_submission and Titanic test files, this comprehensive CSV file forms the backbone of our application. Our goal is to distill key insights from the dataset, offering users an intuitive dashboard to unravel the factors that shaped survival aboard the ill-fated Titanic.')

st.subheader('Aims and Objectives')
st.write('Our dashboard applications ultimate purpose is to increase understanding of the Titanic dataset by striving for accuracy levels higher than 70%. In order to do this, we have three specific objectives: identify the critical factors influencing survival rates, present these findings in easily interpreted charts, and enable users to make informed predictions that may be as accurate as 100%.')


#opening the image
image = Image.open('experience-at-titanic-pigeon-forge.jpg')

#displaying the image on streamlit app
st.image(image, caption='Lets see if you can survive me')

st.subheader('Dataset Overview')

# Read the CSV file into a DataFrame
df = pd.read_csv('tested.csv')

# Display the DataFrame using Streamlit
st.dataframe(df)