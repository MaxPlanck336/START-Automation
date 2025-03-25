import streamlit as st
from utils.graphs import uni_histogram, batch_histogram

from dataloading import DataLoader


df = DataLoader("../Resources/local_db.csv").load_data()


# Set the page to full width
st.set_page_config(layout="wide")

st.markdown("## University")
uni_histogram(df)
batch_histogram(df)
