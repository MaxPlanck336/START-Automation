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

def uni_histogram():

    university_groups = df.groupby("University")
    unis = [name for name, _ in university_groups]
    people_per_uni = [len(group) for _, group in university_groups]

    uni_dict = dict(zip(unis, people_per_uni))

    uni_dict = dict(sorted(uni_dict.items(), key=lambda item: item[1], reverse=False))


    fig, ax = plt.subplots(figsize=(10, 4))
    ax.grid(color='white', linestyle='--', linewidth=0.5, alpha=0.7)
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')
    fig.patch.set_alpha(0.0)
    ax.set_facecolor('none')
    ax.barh(list(uni_dict.keys()), list(uni_dict.values()), color='skyblue')
    ax.set_xlabel("Number of Starties")
    ax.set_title("Number of Starties per University")
    plt.tight_layout()
    st.pyplot(fig)

def batch_histogram():
    batch_groups = df.groupby("Batch")
    batches = [name.replace("SoSe-", "SS-") for name, _ in batch_groups if "SS-" in name.replace("SoSe-", "SS-") or "WS-" in name]
    people_per_batch = [len(group) for name, group in batch_groups if name.replace("SoSe-", "SS-") in batches or name in batches]

    batch_dict = dict(zip(batches, people_per_batch))

    batch_dict = dict(sorted(batch_dict.items(), key=lambda item: (int(item[0].split("-")[1]), item[0].split("-")[0] == "WS"), reverse=False))

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.grid(color='white', linestyle='--', linewidth=0.5, alpha=0.7)
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')
    fig.patch.set_alpha(0.0)
    ax.set_facecolor('none')
    ax.bar(list(batch_dict.keys()), list(batch_dict.values()), color='skyblue')
    ax.set_xlabel("Number of Starties")
    ax.set_title("Number of Starties per Batch")
    plt.tight_layout()
    st.pyplot(fig)