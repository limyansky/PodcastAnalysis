#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:16:53 2024

@author: brent
"""

import pandas as pd
from collections import defaultdict
import numpy as np

df_raw = pd.read_csv("/home/brent/Documents/github/PodcastAnalysis/Data_Products/Intermediate/raw_NoIntro.csv")


# Good for Diagnostics
speaker_counts = df_raw.groupby(['Speaker'])['Speaker'].count().reset_index(name="Lines")
speaker_counts.sort_values(by="Lines", inplace=True, ascending=False)

# Translation Dictionary
speaker_key = {
    "Anthony":"Anthony",
    "Matt":"Matt",
    "Darryl":"Matt",
    "Freddie":"Freddie",
    "Glenn":"Freddie",
    "Will":"Will",
    "Henry":"Will",
    "Beth":"Beth",
    "Ron":"Beth",
    "Young Ron":"Beth",
    "Jimmy":"Jimmy",
    "Jodie":"Jimmy",
    "Jenna":"Jenna",
    "Ratticus":"Jenna",
    "Ashly":"Ashly",
    "Dennis":"Ashly",
    "Mark":"Ashly",
    "Juror":"Juror",
    "Baz Benham Benquin": "Jason"
    }

speaker_dict = defaultdict(lambda:"Anthony", speaker_key)

df_raw.insert(2, "Actor", [speaker_dict[x] for x in df_raw["Speaker"]])
df_raw["Actor"][df_raw["Speaker"].isnull()] = np.nan

df_raw.to_csv("/home/brent/Documents/github/PodcastAnalysis/Data_Products/Intermediate/actors_NoIntro.csv")

actor_counts = df_raw.groupby(['Actor'])['Actor'].count().reset_index(name="Lines")
actor_counts.sort_values(by="Lines", inplace=True, ascending=False)

### Episode 56 ###
# Dungeon Master: Anthony Burch   
# Jodie Foster​: Freddie Wong   
# Henry Oak​: Matt Arnold   
# Ron Stampler​: Will Campos   
# Darryl Wilson​: Beth May  
# Glenn Close: Jimmy Wong  
# Baz Benham Benquin: Jason Boulet - Done

### Episode 57 ### 
# Dungeon Master: Anthony Burch   
# Darryl Wilson: Freddie Wong   
# Ron Stampler: Matt Arnold   
# Glenn Close​: Will Campos   
# Jodie Foster: Beth May  
# Henry Oak: Jimmy Wong
