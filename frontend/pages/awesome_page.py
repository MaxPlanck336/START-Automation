import streamlit as st

import matplotlib.pyplot as plt
from utils.graphs import dep_pie, member_tier, study_program

from dataloading import DataLoader


df = DataLoader("../Resources/local_db.csv").load_data()


st.set_page_config(
        page_title="Departments",
        page_icon="🏢",
    )

st.write("Departments")
dep_pie(df)
member_tier(df)
study_program(df)