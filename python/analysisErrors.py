#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:39:20 2024

@author: brent
"""

import pandas as pd
import matplotlib.pylab as plt
import numpy as np

df_actors = pd.read_csv("/home/brent/Documents/github/PodcastAnalysis/Data_Products/Intermediate/actors_NoIntro.csv")

speaker_counts = df_actors.value_counts("Speaker")

num_speakers = len(speaker_counts)
rnge_speakers = range(num_speakers)

# Number of lines per speaker as a bar chart
plt.bar(rnge_speakers, speaker_counts.values)
plt.title("Lines Per Speaker")
plt.xlim(-1,100)
plt.show()

# Cumulative lines spoken if you include top n speakers
cum_counts = np.cumsum(speaker_counts.values)
plt.plot(rnge_speakers, cum_counts)
plt.title("Cumulative Lines - Top n Speakers")
plt.show()

# Fraction of cumulative lines spoken ifyou include top n speakers
cum_frac = cum_counts/cum_counts[-1]
plt.plot(rnge_speakers, cum_frac)
plt.title("Fraction Cumulative Lines - Top n Speakers")
plt.show()

# How many speakers does it take to reach a certain percentage of lines spoken?
def how_many_speakers(percentage):
    return num_speakers - sum(cum_frac >= percentage)

percentages = np.arange(0, 0.99, 0.01)
speaker_track = []
for ii in percentages:
    speaker_track.append(how_many_speakers(ii))
    
plt.plot(percentages,speaker_track)
plt.title("Number of Speakers Needed to Reach Percentage of Lines Spoken")
plt.show()

# Start with the most prominent speaker.
# What additional fraction of lines do you account for if you include
# the next highest speaker in your counting?
frac_additional = cum_frac[1:] - cum_frac[:-1]
plt.plot(range(1, 16), frac_additional[:15])
plt.title("Additional Percentage Gained from Counting Additional Speaker")
plt.show()

# Errors are mostly here.
# What fraction of the total number of spoken lines come from
# speakers who only ever speak one line?
# about 0.3% of total lines.
# 2 lines - 0.07%.
sum(speaker_counts.values == 1)/cum_counts[-1]


