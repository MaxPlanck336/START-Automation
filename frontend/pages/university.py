import streamlit as st
from utils.graphs import uni_histogram, batch_histogram
# Set the page to full width
st.set_page_config(layout="wide")

st.markdown("## University")
uni_histogram()
batch_histogram()
