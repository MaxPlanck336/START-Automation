import streamlit as st

import matplotlib.pyplot as plt
from utils.graphs import dep_pie

st.set_page_config(
        page_title="Departments",
        page_icon="🏢",
    )

st.write("Departments")
dep_pie()