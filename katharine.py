#! usr/bin/env python3

import re

#Regular expression to match every variant of a name (HOMEWORK ASSIGNMENT 8):
name = 'Kathrin'
#names: katharine, Katherine, Catheryn, Cathryn, Kathryn, Katherine, Catherine, & Kathrin
match = re.search("[KC]ath[ae]*r[iy]ne*", name, re.I)
if match:
	print("Found a match: ", match.group())
else:
	print("No match found.")