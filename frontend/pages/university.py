import streamlit as st
import seaborn as sns
from utils.graphs import uni_histogram, study_program

from dataloading import DataLoader


df = DataLoader("../Resources/local_db.csv").load_data()


# Set the page to full width
st.set_page_config(
        page_title="University Statistics",
        page_icon="📊",
        layout="wide"
    )
st.title("University Statistics")

cmap = sns.color_palette("mako")
uni_histogram(df, cmap)
study_program(df, cmap)
