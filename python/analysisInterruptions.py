#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 23:26:33 2024

@author: brent
"""

import pandas as pd

df_intr = pd.read_csv("/home/brent/Documents/github/PodcastAnalysis/Data_Products/Intermediate/interruptions_NoIntro.csv")
df_intr.drop("Unnamed: 0", axis=1, inplace=True)

# Number of lines from each actor
df_counts = df_intr.groupby(['Actor'])['Actor'].count().reset_index(name="Lines")

# Only the interruptions
df_intr_only = df_intr[df_intr["Interruption"]==True]

# I don't care when a person was interrupted by e.g. laughter
df_intr_only = df_intr_only[pd.isnull(df_intr_only["NextSpeaker"]) == False]

# I don't care when an actor interrupts themselves
df_intr_only = df_intr_only[df_intr_only["NextActor"]!=df_intr_only["Actor"]]

# Count total interruptions
df_intr_counts = df_intr_only.groupby(['Actor'])['Actor'].count().reset_index(name="Lines")

df_cutter_counts = df_intr_only.groupby(['NextActor'])['NextActor'].count().reset_index(name="Lines")

df_counts = pd.merge(df_counts, df_intr_counts, left_on="Actor", right_on="Actor", how="outer")
df_counts = pd.merge(df_counts, df_cutter_counts, left_on="Actor", right_on="NextActor", how="outer")

df_counts.rename(columns={"Lines_x":"Lines", "Lines_y": "Interrupted", "Lines": "Cutter"}, inplace=True)
df_counts.drop(["NextActor"],axis=1, inplace=True)

df_counts["FracInterrupted"] = df_counts["Interrupted"]/df_counts["Lines"]
df_counts["FracCutting"] = df_counts["Cutter"]/df_counts["Lines"]
df_counts["FracTotal"] = df_counts["Lines"]/df_counts["Lines"].sum()
df_counts["FracInterruptedTot"] = df_counts["Interrupted"]/df_counts["Interrupted"].sum()
df_counts["FracCuttingTot"] = df_counts["Cutter"]/df_counts["Cutter"].sum()

