#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:38:19 2024

@author: brent
"""

import glob

# transcript file paths
files = glob.glob('../Daddies_Transcripts/*.md')

# sort by ep. number, assuming format "*Ep. [X OR XX] Episode Name"
# might not handle Ep. 68 Pt. II
files.sort(key = lambda x: int(x.split("Ep. ")[1].split(" ")[0]))

# Marks the start of the non-scripted portion of the podcast
intro_list = ["four dads from our world", 
              "BDSM",
              "\\[*intro music plays*\\]"]

for file in files:
    ep_number = int(file.split("Ep. ")[1].split(" ")[0])
    
    with open(file) as reading:
        for line in reading:
            if any(intro in line for intro in intro_list):
                print(ep_number)
                break
            
        


