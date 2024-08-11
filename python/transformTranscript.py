#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:16:53 2024

@author: brent
"""

import pandas as pd
from collections import defaultdict
import numpy as np

# Input file containing parsed transcript
df_raw = pd.read_csv("/home/brent/Documents/github/PodcastAnalysis/Data_Products/Intermediate/raw_NoIntro.csv")

# Good for Diagnostics
speaker_counts = df_raw.groupby(['Speaker'])['Speaker'].count().reset_index(name="Lines")
speaker_counts.sort_values(by="Lines", inplace=True, ascending=False)

# Translation Dictionary - Which actor corresponds to which speaker?
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

# Special transoation dictionaries for body swap episodes.

### Episode 56 ###
# Dungeon Master: Anthony Burch   
# Jodie Foster​: Freddie Wong   
# Henry Oak​: Matt Arnold   
# Ron Stampler​: Will Campos   
# Darryl Wilson​: Beth May  
# Glenn Close: Jimmy Wong  
# Baz Benham Benquin: Jason Boulet

speaker_key_56 = {
    "Anthony":"Anthony",
    "Matt":"Matt",
    "Henry":"Matt",
    "Freddie":"Freddie",
    "Jodie":"Freddie",
    "Will":"Will",
    "Ron":"Will",
    "Beth":"Beth",
    "Darryl":"Beth",
    "Jimmy":"Jimmy",
    "Glenn":"Jimmy",
    "Baz Benham Benquin": "Jason"
    }

### Episode 57 ### 
# Dungeon Master: Anthony Burch   
# Darryl Wilson: Freddie Wong   
# Ron Stampler: Matt Arnold   
# Glenn Close​: Will Campos   
# Jodie Foster: Beth May  
# Henry Oak: Jimmy Wong

speaker_key_57 = {
    "Anthony":"Anthony",
    "Matt":"Matt",
    "Ron":"Matt",
    "Freddie":"Freddie",
    "Darryl":"Freddie",
    "Will":"Will",
    "Glenn":"Will",
    "Beth":"Beth",
    "Jodie":"Beth",
    "Jimmy":"Jimmy",
    "Henry":"Jimmy",
    "Baz Benham Benquin": "Jason"
    }

# Rather than list every speaker played by Anthony, I default all unlisted
# speakers to Anthony. 
# NOTE: Speaker "nan" is associated with lines like "\[laughter\]", and will be
#       associated with Anthony. This is fixed later in this code.
# NOTE: There are some erronous speakers (from bad parsing) associated with
#       Anthony. This is analyzed as error.
speaker_dict = defaultdict(lambda:"Anthony", speaker_key)
speaker_dict_56 = defaultdict(lambda:"Anthony", speaker_key_56)
speaker_dict_57 = defaultdict(lambda:"Anthony",speaker_key_57)


# Perform the actor look-up
def find_actor(row):
    if row["Episode"] == 56: # Body swap
        return speaker_dict_56[row["Speaker"]]
    elif row["Episode"] == 57: # Body swap
        return speaker_dict_57[row["Speaker"]]
    else: # Normal episode
        return speaker_dict[row["Speaker"]]
    
df_raw["Actor"] = df_raw.apply(find_actor, axis=1)

# Unassign actor "Anthony" speaker "nan" (such as for \[laughter\])
df_raw["Actor"][df_raw["Speaker"].isnull()] = np.nan

# Not entirely sure where this came from
df_raw.drop("Unnamed: 0", axis=1)

# Put columns in more logical order
col_order = ['Episode', 'Actor', 'Speaker', 'Line']
df_raw = df_raw[col_order]

# Save file with actors added
df_raw.to_csv("/home/brent/Documents/github/PodcastAnalysis/Data_Products/Intermediate/actors_NoIntro.csv")

# Adds next actor/speaker columns
df_raw["NextSpeaker"] = df_raw["Speaker"].shift(-1)
df_raw["NextActor"] = df_raw["Actor"].shift(-1)

# Searches for lines ending in interrupt symbol
def find_interrupts(row):
    if str(row["Line"])[-1] == "—":
        return True
    else:
        return False

# Tag lines ending with an interruption
df_raw["Interruption"] = df_raw.apply(find_interrupts, axis=1)

df_raw.to_csv("/home/brent/Documents/github/PodcastAnalysis/Data_Products/Intermediate/interruptions_NoIntro.csv")

# Diagnostics
actor_counts = df_raw.groupby(['Actor'])['Actor'].count().reset_index(name="Lines")
actor_counts.sort_values(by="Lines", inplace=True, ascending=False)


