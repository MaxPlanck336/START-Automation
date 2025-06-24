import streamlit as st
import seaborn as sns

import matplotlib.pyplot as plt
from utils.graphs import dep_pie, member_tier, study_program, uni_histogram, batch_histogram

from dataloading import DataLoader


df = DataLoader("../Resources/responses.csv").load_data()


st.set_page_config(
        page_title="Statistics",
        page_icon="📊",
        layout="wide"
    )



cmap = sns.color_palette("rocket")
# Add padding using Streamlit columns (10% left, 80% center, 10% right)
left, center, right = st.columns([1, 6, 1])
with center:
    # can you create two sections that are collapsable and have a title, one for START statistics and one for university stuff
    st.title("START Statistics")
    dep_pie(df, cmap)
    member_tier(df, cmap)
    batch_histogram(df, cmap)
