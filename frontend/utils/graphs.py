import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def dep_pie(df, colormap="rocket"):
    # Preprocess the data
    dep_names = df["Department"].value_counts().index
    # Remove all special characters that can't be displayed like emojis
    dep_names = ["".join(filter(str.isalnum, name)) for name in dep_names]

    dep_counts = df["Department"].value_counts().values

    sns.set_style("dark")

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_alpha(0.0)

    ax.pie(dep_counts, labels=dep_names, autopct='%1.1f%%', startangle=140, colors=sns.color_palette(colormap, len(dep_counts)))
    ax.set_title("Department Distribution", fontsize=16, color="white")

    # Make text white
    for text in ax.texts:
        text.set_color("white")

    st.pyplot(fig)

def uni_histogram(df, colormap="mako"):
    university_groups = df.groupby("University")
    unis = [name for name, _ in university_groups]
    people_per_uni = [len(group) for _, group in university_groups]

    uni_dict = dict(zip(unis, people_per_uni))

    uni_dict = dict(sorted(uni_dict.items(), key=lambda item: item[1], reverse=True))

    sns.set_style("dark")
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_alpha(0.0)
    sns.barplot(x=list(uni_dict.keys()), y=list(uni_dict.values()), palette=colormap, ax=ax)

    ax.set_facecolor("none")
    ax.set_xlabel("University", color="white")
    ax.set_ylabel("Number of Starties", color="white")
    ax.set_title("Number of Starties per University", fontsize=16, color="white")
    ax.tick_params(axis='x', colors='white', rotation=45)
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.grid(color='white', linestyle='--', linewidth=0.5, alpha=0.7)

    # Add count labels
    for i, v in enumerate(uni_dict.values()):
        ax.text(i, v + 1, str(v), ha='center', color="white")

    plt.tight_layout()
    st.pyplot(fig)

def batch_histogram(df, colormap="mako"):
    people_per_batch = df.groupby(["Which semester did you join?", "Which year did you join?"]).size()
    x = []
    y = []
    for (semester, year), count in people_per_batch.items():
        x.append(f"{semester} {year}")
        y.append(count)
    batch_dict = dict(zip(x, y))
    # sort by year and semester
    batch_dict = dict(sorted(batch_dict.items(), key=lambda item: (item[0].split()[1], item[0].split()[0])))
    # batch_groups = df.groupby("Which semester did you join?")
    # batches = [name.replace("SoSe-", "SS-") for name, _ in batch_groups if "SS-" in name.replace("SoSe-", "SS-") or "WS-" in name]
    # people_per_batch = [len(group) for name, group in batch_groups if name.replace("SoSe-", "SS-") in batches or name in batches]

    # batch_dict = dict(zip(batches, people_per_batch))

    # batch_dict = dict(sorted(batch_dict.items(), key=lambda item: (int(item[0].split("-")[1]), item[0].split("-")[0] == "WS"), reverse=False))

    sns.set_style("dark")
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_alpha(0.0)
    sns.barplot(x=list(batch_dict.keys()), y=list(batch_dict.values()), palette=colormap, ax=ax)

    ax.set_facecolor("none")
    ax.set_xlabel("Batch", color="white")
    ax.set_ylabel("Number of Starties", color="white")
    ax.set_title("Number of Starties per Batch", fontsize=16, color="white")
    ax.tick_params(axis='x', colors='white', rotation=45)
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.grid(color='white', linestyle='--', linewidth=0.5, alpha=0.7)

    # Add count labels
    for i, v in enumerate(batch_dict.values()):
        ax.text(i, v + 1, str(v), ha='center', color="white")

    plt.tight_layout()
    st.pyplot(fig)

def member_tier(df, colormap="rocket"):
    df["Member tier"] = df["Member tier"].str.split(", ")
    df = df.explode("Member tier")
    
    tier_counts = df["Member tier"].value_counts().sort_values()

    sns.set_style("dark")
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_alpha(0.0)
    sns.barplot(x=tier_counts.values, y=tier_counts.index, ax=ax, palette=colormap)

    ax.set_facecolor("none")
    ax.set_title("Member Tier Distribution", fontsize=16, color="white")
    ax.set_xlabel("Count", color="white")
    ax.set_ylabel("Member Tier", color="white")
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Add count labels
    for i, v in enumerate(tier_counts.values):
        ax.text(v + 1, i, str(v), va='center')

    st.pyplot(fig)

def study_program(df, colormap="mako"):
    study_programs_dict = df["Study program name"].value_counts()
    study_programs_dict = study_programs_dict[study_programs_dict > 1]

    # Create a vertical bar plot
    sns.set_style("dark")
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_alpha(0.0)

    x = study_programs_dict.index
    y = study_programs_dict.values
    sns.barplot(x=x, y=y, ax=ax, palette=colormap, dodge=False)

    ax.set_facecolor("none")
    ax.set_xlabel("Study Program", color="white")
    ax.set_ylabel("Count", color="white")
    ax.set_title("Study Program Distribution", fontsize=16, color="white")
    ax.tick_params(axis='x', colors='white', rotation=45)
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.grid(color='white', linestyle='--', linewidth=0.5, alpha=0.7)

    # Add count labels
    for i, v in enumerate(y):
        ax.text(i, v + 1, str(v), ha='center', color="white")

    plt.tight_layout()
    st.pyplot(fig)

    # Add another plot with all the other study programs in form of a list
    other_study_programs = df["Study program name"].value_counts()
    other_study_programs = other_study_programs[other_study_programs <= 1]
    
    st.write("Other Study Programs:")
    st.write(other_study_programs.index)
