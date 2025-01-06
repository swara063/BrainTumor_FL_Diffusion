import streamlit as st
import sys

# Set the title of the app
st.title("Python Version Check")

# Get the Python version
python_version = sys.version

# Display the Python version
st.write(f"The current Python version is: **{python_version}**")
