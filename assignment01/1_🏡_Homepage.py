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

# Introduction and Aims and Objectives
introduction_col, gif_col = st.columns([2, 1])

# Introduction
introduction_col.header('Intro')
introduction_col.write('Explore the depths of history with our Titanic Dashboard Application, an insightful tool born from the Titanic dataset sourced from Kaggle\'s beginner competition. Meticulously crafted by combining gender_submission and Titanic test files, this comprehensive CSV file forms the backbone of our application. Our goal is to distill key insights from the dataset, offering users an intuitive dashboard to unravel the factors that shaped survival aboard the ill-fated Titanic.')

# Aims and Objectives
introduction_col.subheader('Aims and Objectives')
introduction_col.write('Our dashboard application\'s ultimate purpose is to increase understanding of the Titanic dataset by striving for accuracy levels higher than 70%. In order to do this, we have three specific objectives: identify the critical factors influencing survival rates, present these findings in easily interpreted charts, and enable users to make informed predictions that may be as accurate as 100%.')

# Image (GIF)
gif_col.image('QWx3qZ.gif', use_column_width=True)

# Dataset Overview
st.subheader('Dataset Overview')
st.dataframe(df_train)

# Filter by Survival for Visualization: Age Distribution
survival_filter = st.selectbox("Filter by Survival (Age Distribution)", options=['All', 'Survived', 'Not Survived'])
filtered_data_age = df_train.copy()

# Apply filters
if survival_filter != 'All':
    filtered_data_age = filtered_data_age[filtered_data_age['Survived'] == (1 if survival_filter == 'Survived' else 0)]

# Visualization 1: Age Distribution by Survival
age_chart = alt.Chart(filtered_data_age).mark_bar().encode(
    x=alt.X('Age:Q', bin=True),
    y='count()',
    color='Survived:N',
    tooltip=['Survived:N', 'count()']
).properties(title='Age Distribution by Survival')

# Use ChartBuilder for interactivity
age_chart = st.altair_chart(age_chart, use_container_width=True)

# Visualization 2 and 3: Age and Pclass Distribution (Side by Side)
col1, col2 = st.columns(2)

# Filter by Pclass for Visualization 2
pclass_filter_2 = col1.selectbox("Filter by Pclass (Visualization 2)", options=['All'] + list(df_train['Pclass'].unique()))
filtered_data_age_pclass = df_train if pclass_filter_2 == 'All' else df_train[df_train['Pclass'] == pclass_filter_2]

# Visualization 2: Age Distribution
age_chart_pclass = alt.Chart(filtered_data_age_pclass).mark_bar().encode(
    alt.X("Age:Q", bin=True),
    y='count()',
    tooltip=['count()']
).properties(title='Age Distribution')
col1.altair_chart(age_chart_pclass)

# Filter by Pclass for Visualization 3
pclass_filter_3 = col2.selectbox("Filter by Pclass (Visualization 3)", options=['All'] + list(df_train['Pclass'].unique()))
filtered_data_pclass = df_train if pclass_filter_3 == 'All' else df_train[df_train['Pclass'] == pclass_filter_3]

# Visualization 3: Pclass Distribution
pclass_chart = alt.Chart(filtered_data_pclass).mark_bar().encode(
    x='Pclass:O',
    y='count()',
    tooltip=['Pclass:O', 'count()']
).properties(title='Pclass Distribution')
col2.altair_chart(pclass_chart)

# Visualization 5: Age Distribution Histogram
survival_filter_5 = st.selectbox("Filter by Survival (Visualization 4)", options=['All', 'Survived', 'Not Survived'])

filtered_data_age_hist = df_train.copy()

# Apply filters
if survival_filter_5 != 'All':
    filtered_data_age_hist = filtered_data_age_hist[filtered_data_age_hist['Survived'] == (1 if survival_filter_5 == 'Survived' else 0)]

# Visualization 5: Age Distribution Histogram
age_hist_chart = alt.Chart(filtered_data_age_hist).mark_bar().encode(
    x=alt.X('Age:Q', bin=True, title='Age'),
    y='count()',
    color='Survived:N',
    column='Sex:N',
    tooltip=['Age:Q', 'count()', 'Survived:N', 'Sex:N']
).properties(title='Age Distribution Histogram')

st.altair_chart(age_hist_chart)

# Visualization 4 and 6: SibSp and Parch Distribution and Embarked Distribution (Side by Side)
col3, col4 = st.columns(2)

# Filter by Parch for Visualization 4
parch_filter = col3.selectbox("Filter by Parch (Visualization 5)", options=['All'] + list(df_train['Parch'].unique()))
filtered_data_parch = df_train if parch_filter == 'All' else df_train[df_train['Parch'] == parch_filter]

# Visualization 4: SibSp and Parch Distribution (Bar Chart)
sibsp_chart = alt.Chart(filtered_data_parch).mark_bar().encode(
    x=alt.X('SibSp:O', title='SibSp'),
    y='count()',
    color='Sex:N',
    column='Parch:O',
    tooltip=['SibSp:O', 'Parch:O', 'Sex:N', 'count()']
).properties(title='SibSp and Parch Distribution (Bar Chart)')

col3.altair_chart(sibsp_chart)

# Filter by Survival for Visualization 6
survival_filter_6 = col4.selectbox("Filter by Survival (Visualization 6)", options=['All', 'Survived', 'Not Survived'])
filtered_data_embarked = df_train.copy()

# Apply filters
if survival_filter_6 != 'All':
    filtered_data_embarked = filtered_data_embarked[filtered_data_embarked['Survived'] == (1 if survival_filter_6 == 'Survived' else 0)]

# Visualization 6: Embarked Distribution
embarked_chart = alt.Chart(filtered_data_embarked).mark_bar().encode(
    x='Embarked:O',
    y='count()',
    tooltip=['Embarked:O', 'count()']
).properties(title='Embarked Distribution')

col4.altair_chart(embarked_chart)
