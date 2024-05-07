"""
Interactive demonstration of DD-SIMCA.
Author: Nathan A. Mahynski
"""
import sklearn
import pandas as pd
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(layout="wide")

with st.sidebar:
    st.title('DD-SIMCA: Data-Driven Soft Independent Modeling of Class Analogies')
    st.markdown('''
    ## About this application
    This tool uses the [PyChemAuth](https://pychemauth.readthedocs.io/en/latest/index.html) python package for analysis.
    ''')
    add_vertical_space(2)
    st.write('Made by ***Nate Mahynski***')
    st.write('nathan.mahynski@nist.gov')

st.write("Start by uploading some data to model.")

uploaded_file = st.file_uploader(
  label="Upload a CSV file. Observations should be in rows, while columns should correspond to different features",
  type=['csv'], accept_multiple_files=False, 
  key=None, help="", 
  on_change=None, label_visibility="visible")

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.dataframe(dataframe)

    target_column = st.selectbox(label="Select a column as the target class.", options=dataframe.columns, index=0, placeholder="Select a column", disabled=False, label_visibility="visible")
    target_class = st.selectbox(label="Select a class to model.", options=dataframe[target_class].unique(), index=0, placeholder="Select a class", disabled=False, label_visibility="visible")
    random_state = st.number_input(label="Random seed", min_value=None, max_value=None, value=42, step=1, placeholder="Seed", disabled=False, label_visibility="visible")
    test_size = st.slider(label="Fraction of data to use as test set", min_value=0.0, max_value=1.0, value=0.2, step=0.05, disabled=False, label_visibility="visible")

    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
      dataframe[dataframe.columns != target_column],
      dataframe[target_column],
      shuffle=True,
      random_state=random_state,
      test_size=test_size,
      stratify=dataframe[target_column]
      )

    alpha = st.number_input(label=r"Type I Error Rate ($\alpha$)", min_value=0, max_value=1, value=0.05, step=0.01, placeholder=r"$\alpha$", disabled=False, label_visibility="visible")

    # add tabs to display test, train data, analysis

if __name__ == "__main__":
  print('ddsimca')
