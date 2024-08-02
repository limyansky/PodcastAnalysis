# PodcastAnalysis
Analyzing transcripts from the "Dungeons and Daddies" podcast to find metrics such as the number of times a speaker was interrupted.

# Analysis Notes
The podcast opening is often a scripted comedy bit.
The format varies, but you may have a single character giving a monolog for several paragraphs, or brand new characters who occur exclusively in the opening.
I don't want to include this portion in my analysis, so I look for indicators that the non-scripted portion has begun. 
I initially tried looking for the theme song, but this was not consistently denoted across transcripts.
The spoken introduction at the end of the scripted comedy generally goes along the lines of "Welcome to Dungeons and Daddies, not a BDSM podcast, about four dads from our world flung into the Forgotten Realms on a quest to rescue their lost sons". 
There is some variation across episode openings, but searching for the terms "four dads from our world" or "BDSM" successfully identifies the introduction for all but Ep. 68 Pt. II.
For this edge case, I search for "Welcome to the conclusion of season one".
