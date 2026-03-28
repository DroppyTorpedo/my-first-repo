#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
	print(f"positive\n")
else number < 0:
	print(f"negative\n")
else number == 0:
	print(f"zero\n")
else:
	printf(f"wrong type\n")