import pandas as pd
import numpy as np
import streamlit as st

st.title("Filter here.")

Titanic = pd.read_csv("CleanTitanicDataset.csv")

st.radio('Pick your gender', ['Male', 'Female'])