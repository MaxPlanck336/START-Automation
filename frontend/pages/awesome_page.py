import streamlit as st

import matplotlib.pyplot as plt
from utils.graphs import dep_pie, member_tier
import pandas as pd

df = pd.read_csv("../Resources/local_db.csv")

st.set_page_config(
        page_title="Departments",
        page_icon="🏢",
    )

st.write("Departments")
dep_pie(df)

st.write("Member Tier")
member_tier(df)