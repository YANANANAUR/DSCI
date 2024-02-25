import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Realatives")
st.markdown('how many people would you bring?')

# Load your data (replace this with your actual data loading code)
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# Preprocess data
data = [train_data, test_data]
for dataset in data:
    dataset['relatives'] = dataset['SibSp'] + dataset['Parch']
    dataset.loc[dataset['relatives'] > 0, 'travelled_alone'] = 'No'
    dataset.loc[dataset['relatives'] == 0, 'travelled_alone'] = 'Yes'

# Create Streamlit app
st.title("Survival Analysis based on Relatives")

# Select chart type using radio buttons
chart_type = st.radio("Select Chart Type:", ["Bar Chart", "Scatter Plot"])

if chart_type == "Bar Chart":
    # Use seaborn to create a bar chart
    st.subheader("Bar Chart")
    fig, ax = plt.subplots()
    sns.barplot(x='relatives', y='Survived', data=train_data, ax=ax)
    st.pyplot(fig)

elif chart_type == "Scatter Plot":
    # Use Altair to create a scatter plot
    st.subheader("Scatter Plot")
    chart = alt.Chart(train_data).mark_circle().encode(
        x='relatives:O',
        y='Survived:Q',
        tooltip=['relatives', 'Survived']
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

# Create Streamlit app
st.title("Interactive Scatter Plot")

# Select columns using multiselect widget
x_column = st.selectbox("Select X-axis column:", train_data.columns)
y_column = st.selectbox("Select Y-axis column:", train_data.columns)
color_column = st.selectbox("Select Color column:", train_data.columns)

# Create Altair scatter plot
scatter_chart = alt.Chart(train_data).mark_circle().encode(
    x=x_column,
    y=y_column,
    color=color_column,
    tooltip=list(train_data.columns)
).interactive()

# Display the chart using Altair
st.altair_chart(scatter_chart, use_container_width=True)