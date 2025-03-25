import streamlit as st
from dataloading import DataLoader

df = DataLoader("../Resources/local_db.csv").load_data()

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    df.head().to_markdown()
)