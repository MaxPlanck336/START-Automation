from dataloading import DataLoader
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def dep_pie(df):
    # Preprocess the data
    dep_names = df["Department"].value_counts().index
    # Remove all special characters that can't be displayed like emojis
    dep_names = ["".join(filter(str.isalnum, name)) for name in dep_names]

    dep_counts = df["Department"].value_counts().values

    def format_label(val):
        total = sum(dep_counts)
        count = int(round(val / 100 * total))
        return f"{count} ({val:.1f}%)"

    sns.set_style("dark")
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_alpha(0.0)

    wedges, texts, autotexts = ax.pie(
        dep_counts, labels=dep_names, autopct=format_label, colors=sns.color_palette("rocket", len(dep_names))
    )

    for autotext in autotexts:
        autotext.set_color("white")
        autotext.set_fontsize(10)
    for text in texts:
        text.set_color("white")
        text.set_fontsize(12)

    ax.set_title("Department Distribution", fontsize=16, color="white")
    st.pyplot(fig)


def member_tier(df):
    df["Member Tier"] = df["Member Tier"].str.split(", ")
    df = df.explode("Member Tier")
    
    tier_counts = df["Member Tier"].value_counts().sort_values()

    sns.set_style("dark")
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_alpha(0.0)
    sns.barplot(x=tier_counts.values, y=tier_counts.index, ax=ax, palette="rocket")

    ax.set_facecolor("none")
    ax.set_title("Member Tier Distribution", fontsize=16, color="white")
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Add count labels
    for i, v in enumerate(tier_counts.values):
        ax.text(v + 1, i, str(v), va='center')

    st.pyplot(fig)




