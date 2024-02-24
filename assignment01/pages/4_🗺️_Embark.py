import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns

class SurvivalAnalysis:
    def __init__(self, train_data, test_data):
        self.train_data = train_data
        self.test_data = test_data
        self.selected_class = None

    def handle_missing_values(self):
        embarked_mode = self.train_data['Embarked'].mode()[0]
        data = [self.train_data, self.test_data]

        for dataset in data:
            dataset['Embarked'] = dataset['Embarked'].fillna(embarked_mode)

    def visualize_data(self):
        sns.set(style="darkgrid")
        sns.countplot(x='Survived', data=self.train_data, hue="Embarked", palette="Set1")

    def streamlit_app(self):
        st.title("Survival Analysis")
        st.subheader("Explore survival data")

        # Filter data based on selected class
        filtered_data = self.train_data[self.train_data['Survived'] == (self.selected_class == 'Survive')]

        # Display filtered data
        st.write(f"Displaying data for {self.selected_class} passengers:")
        st.write(filtered_data)

        # Altair chart for additional visualization
        chart = alt.Chart(filtered_data).mark_bar().encode(
            x='Embarked',
            y='count()',
            color='Embarked'
        ).properties(
            width=600,
            height=400
        )

        st.altair_chart(chart, use_container_width=True)

# Example usage
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# Create instance of SurvivalAnalysis
survival_analysis = SurvivalAnalysis(train_data, test_data)

# Handle missing values
survival_analysis.handle_missing_values()

# Visualize data
survival_analysis.visualize_data()

# Streamlit app context
with st.form(key='my_form'):
    st.title("Survival Analysis")
    st.subheader("Explore survival data")

    # Selectbox for choosing class ticket
    selected_class = st.selectbox('Choose your class ticket', ['Survive', 'Not survive'])

    # Set the selected class in the SurvivalAnalysis instance
    survival_analysis.selected_class = selected_class

    # Form submission button
    submit_button = st.form_submit_button(label='Submit')

# Run the Streamlit app
survival_analysis.streamlit_app()
