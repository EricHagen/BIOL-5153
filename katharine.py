#! usr/bin/env python3

import re

#Regular expression to match every variant of a name (HOMEWORK ASSIGNMENT 8):
name = 'katharine'
#other names: Katherine, Catheryn, Cathryn, Kathryn, Katherine, Catherine, & Kathrin
match = re.search("[KC]ath([ae]*)r[iy]n(e*)", name, re.I)
if match:
	print("Found a match: ", match.group())