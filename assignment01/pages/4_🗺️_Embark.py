import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns

# Sample data for demonstration
train_data = sns.load_dataset("titanic")

# Streamlit app
st.title("Titanic Survival Visualization")

# Filter for Embarked
embarked_filter = st.selectbox("Select Embarked", train_data["embarked"].unique())

# Altair plot
chart = alt.Chart(train_data[train_data["embarked"] == embarked_filter]).mark_bar().encode(
    x='count():O',
    y='survived:N',
    color='embarked:N',
).properties(
    width=600,
    height=300
)

# Display Altair chart with Streamlit
st.altair_chart(chart, use_container_width=True)

# Sample data for demonstration
train_data = sns.load_dataset("titanic")
test_data = sns.load_dataset("titanic")  # Assuming you have a 'test_data' variable

# Impute missing values for 'Embarked'
embarked_mode = train_data['embarked'].mode()
data = [train_data, test_data]
for dataset in data:
    dataset['embarked'] = dataset['embarked'].fillna(embarked_mode[0])

# Streamlit app
st.title("Survival Analysis by Pclass, Sex, and Embarked")

# Filter for gender
gender_filter = st.selectbox("Select Gender", ["All", "Male", "Female"])

# Filter for embarked
embarked_filter = st.selectbox("Select Embarked", ["All"] + train_data["embarked"].unique().tolist())

# Filter data based on gender and embarked
filtered_data = train_data
if gender_filter != "All":
    filtered_data = filtered_data[filtered_data["sex"] == gender_filter.lower()]

if embarked_filter != "All":
    filtered_data = filtered_data[filtered_data["embarked"] == embarked_filter]

# Altair bar chart
chart = alt.Chart(filtered_data).mark_bar().encode(
    x=alt.X('pclass:N', title='Pclass'),
    y=alt.Y('average(survived):Q', title='Survival Rate'),
    color='sex:N',
    column='embarked:N'
).properties(
    width=200,
    height=200
)

# Display Altair chart with Streamlit
st.altair_chart(chart, use_container_width=True)