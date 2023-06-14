import pandas as pd
import os


def get_data(PATH):
    df = pd.read_csv(PATH)
    return df

def get_olympic_data(PATH):
    df = get_data(PATH)
    df["Medal"] = df["Medal"].fillna("NO INFO")
    medals = df[df["Medal"]!="NO INFO"].copy()
    medals = medals.groupby(["Team","Medal"])[["Team"]].count()
    medals.rename(columns={"Team":"Count"},inplace=True)
    medals.reset_index(inplace=True)
    medals.sort_values("Count",ascending=False, inplace=True)
    return medals.iloc[:20]

