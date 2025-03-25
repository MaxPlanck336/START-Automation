from dataloading import DataLoader
import streamlit as st
import matplotlib.pyplot as plt

df = DataLoader("../Resources/local_db.csv").load_data()

def dep_pie():
    # Preprocess the data
    dep_names = df["Department"].value_counts().index
    # remove all special characters that cant be displayed like emojis
    dep_names = ["".join(filter(str.isalnum, name)) for name in dep_names]

    dep_counts = df["Department"].value_counts().values


    def format_label(val):
        total = sum(dep_counts)
        count = int(round(val / 100 * total))
        return f"{count} ({val:.1f}%)"

    fig, ax = plt.subplots()

    fig.patch.set_alpha(0.0)


    _, texts, autotexts = ax.pie(dep_counts, labels=dep_names, autopct=format_label)
    for autotext in autotexts:
        autotext.set_color("white")
    for text in texts:
        text.set_color("white")

    st.pyplot(fig)






