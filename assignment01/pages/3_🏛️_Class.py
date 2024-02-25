import streamlit as st
import pandas as pd
import altair as alt

# Set the style for Altair plots
alt.themes.enable('default')

# Load the data
train_data = pd.read_csv("train.csv")

# Create a Streamlit app
st.title("Survival Analysis")

# Filter by class ticket
selected_class = st.selectbox('Choose your class ticket', ['Survived', 'Not Survived'])

# Filter the data based on the selected class
filtered_data = train_data[train_data['Survived'] == (selected_class == 'Survived')]

# Plot using Altair
chart = alt.Chart(filtered_data).mark_bar().encode(
    x=alt.X('Pclass:O', title='Pclass'),
    y=alt.Y('count()', title='Count'),
    color=alt.Color('Survived:N', scale=alt.Scale(range=['#FF595E', '#8AC926']), legend=alt.Legend(title="Outcome")),
).properties(
    width=600,
    height=400,
    title=f'Distribution of Pclass for {selected_class} Passengers'
)

# Show the Altair chart using Streamlit
st.altair_chart(chart, use_container_width=True)

# Filter by gender
show_all_genders = st.checkbox('Show All Genders', value=True)
if show_all_genders:
    filtered_df = train_data.copy()
else:
    selected_gender = st.selectbox('Choose your gender', ['Male', 'Female'])
    filtered_df = train_data[train_data['Sex'] == selected_gender]

# Plot using Altair
chart_gender = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('Pclass:O', title='Pclass'),
    y=alt.Y('count()', title='Count'),
    color=alt.Color('Sex:N', scale=alt.Scale(range=['#FF595E', '#8AC926']), legend=alt.Legend(title="Gender")),
).properties(
    width=600,
    height=400,
    title=f'Distribution of Pclass by Gender{" (All Genders)" if show_all_genders else f" ({selected_gender} Passengers)"}'
)

# Show the Altair chart using Streamlit
st.altair_chart(chart_gender, use_container_width=True)