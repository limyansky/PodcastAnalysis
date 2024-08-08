#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 12:21:35 2024

@author: brent
"""

import pandas as pd
import matplotlib.pylab as plt
import numpy as np

df_actors = pd.read_csv("/home/brent/Documents/github/PodcastAnalysis/Data_Products/Intermediate/actors_NoIntro.csv")

anthony = []
beth = []
freddie = []
matt = []
will = []


# Count the number of lines for each speaker, per episode
for ep in range(1,70):
    df_episode = df_actors.loc[df_actors["Episode"] == ep]
    actor_counts = df_episode.groupby(['Actor'])['Actor'].count().reset_index(name="Lines")
    
    anthony.append(int(actor_counts[actor_counts["Actor"]=="Anthony"]["Lines"]))
    beth.append(int(actor_counts[actor_counts["Actor"]=="Beth"]["Lines"]))
    freddie.append(int(actor_counts[actor_counts["Actor"]=="Freddie"]["Lines"]))
    matt.append(int(actor_counts[actor_counts["Actor"]=="Matt"]["Lines"]))
    will.append(int(actor_counts[actor_counts["Actor"]=="Will"]["Lines"]))
    
episodes = list(range(1, 70))

# Plot number of lines per episode
plt.plot(episodes, anthony, label="Anthony")
plt.plot(episodes, beth, label="Beth")
plt.plot(episodes, freddie, label = "Freddie")
plt.plot(episodes, matt, label="Matt")
plt.plot(episodes, will, label="Will")
plt.legend()
plt.show()

# Fraction of each episode's lines spoken by each
anthony_frac = []
beth_frac = []
freddie_frac = []
matt_frac = []
will_frac = []

for a, b, f, m, w in zip(anthony, beth, freddie, matt, will):
    total = (a + b + f + m + w)
    anthony_frac.append(a/total)
    beth_frac.append(b/total)
    freddie_frac.append(f/total)
    matt_frac.append(m/total)
    will_frac.append(w/total)
    
plt.plot(episodes, anthony_frac, label="Anthony")
plt.plot(episodes, beth_frac, label="Beth")
plt.plot(episodes, freddie_frac, label = "Freddie")
plt.plot(episodes, matt_frac, label="Matt")
plt.plot(episodes, will_frac, label="Will")
plt.legend()
plt.show()
    
episodes = np.array(episodes)
anthony_frac = np.array(anthony_frac)
beth_frac = np.array(beth_frac)
freddie_frac = np.array(freddie_frac)
matt_frac = np.array(matt_frac)
will_frac = np.array(will_frac)

print(episodes[anthony_frac==max(anthony_frac)])
