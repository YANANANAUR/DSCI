import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

# Set page config
st.set_page_config(
    page_title="CAN YOU SURVIVE?",
    page_icon="🛳️",
    layout="wide",
)

# Load data
train_data = pd.read_csv("train.csv")
df_train = pd.read_csv("train.csv")

# Main Dashboard
st.title('Can You survive the Titanic?')
st.markdown('This application will predict whether you will survive on the Titanic')

# Introduction
st.header('Intro')
st.write('Explore the depths of history with our Titanic Dashboard Application, an insightful tool born from the Titanic dataset sourced from Kaggle\'s beginner competition. Meticulously crafted by combining gender_submission and Titanic test files, this comprehensive CSV file forms the backbone of our application. Our goal is to distill key insights from the dataset, offering users an intuitive dashboard to unravel the factors that shaped survival aboard the ill-fated Titanic.')

# Aims and Objectives
st.subheader('Aims and Objectives')
st.write('Our dashboard application\'s ultimate purpose is to increase understanding of the Titanic dataset by striving for accuracy levels higher than 70%. In order to do this, we have three specific objectives: identify the critical factors influencing survival rates, present these findings in easily interpreted charts, and enable users to make informed predictions that may be as accurate as 100%.')

# Display the image
image = Image.open('experience-at-titanic-pigeon-forge.jpg')
st.image(image, caption='Let\'s see if you can survive me')

# Dataset Overview
st.subheader('Dataset Overview')
st.dataframe(df_train)

# Apply filters
if survival_filter != 'All':
    filtered_data_age = filtered_data_age[filtered_data_age['Survived'] == (1 if survival_filter == 'Survived' else 0)]

if gender_filter != 'All':
    filtered_data_age = filtered_data_age[filtered_data_age['Sex'] == gender_filter]

# Visualization: Age Distribution by Survival and Gender
age_chart = alt.Chart(filtered_data_age).mark_bar().encode(
    x=alt.X('Age:Q', bin=True),
    y='count()',
    color='Survived:N',
    column='Sex:N',
    tooltip=['Sex:N', 'Survived:N', 'count()']
).properties(title='Age Distribution by Survival and Gender')

# Use ChartBuilder for interactivity
age_chart = st.altair_chart(age_chart, use_container_width=True)

# Filter by Pclass for Visualization 2
pclass_filter_2 = st.selectbox("Filter by Pclass (Visualization 2)", options=['All'] + list(df_train['Pclass'].unique()))
filtered_data_age = df_train if pclass_filter_2 == 'All' else df_train[df_train['Pclass'] == pclass_filter_2]

# Visualization 2: Age Distribution
age_chart = alt.Chart(filtered_data_age).mark_bar().encode(
    alt.X("Age:Q", bin=True),
    y='count()',
    tooltip=['count()']
).properties(title='Age Distribution')
st.altair_chart(age_chart)

# Filter by Pclass for Visualization 3
pclass_filter_2 = st.selectbox("Filter by Pclass (Visualization 3)", options=['All'] + list(df_train['Pclass'].unique()))
filtered_data_pclass = df_train if pclass_filter_2 == 'All' else df_train[df_train['Pclass'] == pclass_filter_2]

# Visualization 3: Pclass Distribution
pclass_chart = alt.Chart(filtered_data_pclass).mark_bar().encode(
    x='Pclass:O',
    y='count()',
    tooltip=['Pclass:O', 'count()']
).properties(title='Pclass Distribution')
st.altair_chart(pclass_chart)

# Filter by Sex for Visualization 4
sex_filter = st.selectbox("Filter by Sex", options=['All', 'Male', 'Female'])
filtered_data_sex = df_train if sex_filter == 'All' else df_train[df_train['Sex'] == sex_filter]

# Visualization: SibSp and Parch Distribution
sibsp_parch_chart = alt.Chart(filtered_data_sex).mark_circle().encode(
    x='SibSp:O',
    y='Parch:O',
    color='Sex:N',
    tooltip=['SibSp:O', 'Parch:O', 'Sex:N']
).properties(title='SibSp and Parch Distribution')

st.altair_chart(sibsp_parch_chart)

# Filter by Gender for Visualization 5
gender_filter = st.selectbox("Filter by Gender (Visualization 5)", options=['All', 'Male', 'Female'])
filtered_data_sibsp = df_train if gender_filter == 'All' else df_train[df_train['Sex'] == gender_filter]

# Visualization 5: SibSp and Parch Distribution
sibsp_chart = alt.Chart(filtered_data_sibsp).mark_circle().encode(
    x='SibSp:O',
    y='Parch:O',
    color='Sex:N',
    tooltip=['SibSp:O', 'Parch:O', 'Sex:N']
).properties(title='SibSp and Parch Distribution')

st.altair_chart(sibsp_chart)

# Filter by Survival for Visualization 6
survival_filter = st.selectbox("Filter by Survival (Visualization 6)", options=['All', 'Survived', 'Not Survived'])
filtered_data_embarked = df_train if survival_filter == 'All' else df_train[df_train['Survived'] == (1 if survival_filter == 'Survived' else 0)]

# Visualization 6: Embarked Distribution
embarked_chart = alt.Chart(filtered_data_embarked).mark_bar().encode(
    x='Embarked:O',
    y='count()',
    tooltip=['Embarked:O', 'count()']
).properties(title='Embarked Distribution')
st.altair_chart(embarked_chart)
