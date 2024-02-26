import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px

class GenderSurvivalAnalysis:
    def __init__(self, train_data):
        self.train_data = train_data

    def fill_missing_age(self):
        mean = self.train_data["Age"].mean()
        std = self.train_data["Age"].std()
        is_null = self.train_data["Age"].isnull().sum()
        rand_age = np.random.randint(mean - std, mean + std, size=is_null)
        age_slice = self.train_data["Age"].copy()
        age_slice[np.isnan(age_slice)] = rand_age
        self.train_data["Age"] = age_slice.astype(int)

    def apply_filters(self, gender_filter, survival_filter):
        filtered_data = self.train_data.copy()

        if gender_filter != 'All':
            filtered_data = filtered_data[filtered_data['Sex'] == gender_filter.lower()]

        if survival_filter:
            filtered_data = filtered_data[filtered_data['Survived'].isin([1 if 'Survived' in survival_filter else 0])]

        return filtered_data

    def plot_age_distribution(self, filtered_data):
        st.subheader("Distribution of Age by Gender and Survival Status")

        chart = alt.Chart(filtered_data).mark_bar().encode(
            x=alt.X("Age:Q", bin=True),
            y='count()',
            color=alt.Color('Survived:N', scale=alt.Scale(range=['red', 'green']), title='Survival Status')
        ).properties(
            title=f'Distribution of Age by Gender and Survival Status'
        )

        st.altair_chart(chart, use_container_width=True)

class SurvivalAnalysis:
    def __init__(self, df):
        self.df = df

    def apply_filters(self, survival_filter):
        if survival_filter != 'All':
            survival_value = 1 if survival_filter == 'Survived' else 0
            self.df = self.df[self.df['Survived'] == survival_value]

    def plot_scatter(self):
        st.subheader("Scatter Plot of Age vs. PassengerId with Survival Status")

        fig = px.scatter(self.df, x="PassengerId", y="Age", color="Survived",
                         log_x=True, size_max=20, template="plotly", title="Which Age Survived?")
        st.plotly_chart(fig)


# Load data for GenderSurvivalAnalysis
train_data = pd.read_csv("train.csv")

# Create instance of GenderSurvivalAnalysis
gender_survival_analysis = GenderSurvivalAnalysis(train_data)

# Fill missing Age values
gender_survival_analysis.fill_missing_age()

# Streamlit App for GenderSurvivalAnalysis
st.title("Gender Survival Analysis")

# Filter data based on user selection
gender_filter = st.selectbox("Select Gender", ['All', 'Female', 'Male'], index=0)
survival_filter_gender = st.multiselect("Select Survival Status", ['Survived', 'Not Survived'], default=['Survived', 'Not Survived'])

# Apply filters to the data
filtered_data_gender = gender_survival_analysis.apply_filters(gender_filter, survival_filter_gender)

# Plot Age distribution
gender_survival_analysis.plot_age_distribution(filtered_data_gender)


# Load data for SurvivalAnalysis
df = pd.read_csv("tested.csv")

# Create instance of SurvivalAnalysis
survival_analysis = SurvivalAnalysis(df)

# Streamlit App for SurvivalAnalysis
st.title("Survival Analysis")

# Filter data based on user selection
survival_filter = st.selectbox("Select Survival Status", ['All', 'Survived', 'Not Survived'], index=0)
survival_analysis.apply_filters(survival_filter)

# Plot scatter plot
survival_analysis.plot_scatter()
