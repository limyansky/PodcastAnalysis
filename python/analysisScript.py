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
files.sort(key = lambda x: int(x.split("Ep. ")[1].split(" ")[0]))


