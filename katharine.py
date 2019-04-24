#! usr/bin/env python3

import re

#Regular expression to match every variant of a name (HOMEWORK ASSIGNMENT 8):
print("\nThis is my story:\n")
story = '"Katherine went to the concert to see her favorite band, Catheryn and the Cathryn’s. She ran into her friend Kathryn, who introduced Katherine to her friend, Catherine. Together, they enjoyed the concert while texting inaudible snippets to their mutual friends, Kathrin and katharine."'
print(story)
pattern = "[KC]ath[ae]*r[iy]ne*"
print("\nThese are my matches:")
matches = re.findall(pattern, story, re.I)
print(matches)