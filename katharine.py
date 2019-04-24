#! usr/bin/env python3

import re

#Regular expression to match every variant of a name (HOMEWORK ASSIGNMENT 8):
names = 'katharine, Katherine, Catheryn, Cathryn, Kathryn, Katherine, Catherine, Kathrin'
print("This is my list of names: " + names)
pattern = "[KC]ath[ae]*r[iy]ne*"
print("\nThese are my matches: ")
for match in re.finditer(pattern, names, re.I):
	print(match.group())