#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:38:19 2024

@author: brent
"""

import glob
from collections import defaultdict

# transcript file paths
files = glob.glob('../Daddies_Transcripts/*.md')

# sort by ep. number, assuming format "*Ep. [X OR XX] Episode Name"
# might not handle Ep. 68 Pt. II
files.sort(key = lambda x: int(x.split("Ep. ")[1].split(" ")[0]))

# Marks the start of the non-scripted portion of the podcast
intro_list = ["four dads from our world", 
              "BDSM",
              "Welcome to the conclusion of season one"]

# Holds the number of speaker occurances
speaker_count = defaultdict(lambda:0)
episode_count = defaultdict(lambda:0)
length_one    = defaultdict(lambda:0) # A lot of sound effects. Finishing sentences.

for file in files:
    ep_number = int(file.split("Ep. ")[1].split(" ")[0])
    
    with open(file) as reading:
        in_body = False
        for line in reading:
            if in_body:
                line = line.replace("*","")
                line = line.strip()
                line = line.split(':')
                if len(line) == 1:
                    length_one[line[0]]+=1
                elif len(line) == 2:
                    speaker_count[line[0]]+=1
                    episode_count[ep_number]+=1
            if any(intro in line for intro in intro_list):
                in_body=True

#speaker_count = dict(sorted(speaker_count.items(), key=lambda item: 1/item[1]))

# Count how many interruptions we are missing by not counting double lines
counter = 0
for key in length_one.keys():
    try:
        if key[-1]=='—':
            print(key)
            counter+=1
    except:
        pass
print(counter)