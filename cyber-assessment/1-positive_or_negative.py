#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
	print(f"{number} positive\n")
else number < 0:
	print(f"{number} negative\n")
else number == 0:
	print(f"{number} zero\n")
else:
	printf(f"wrong type\n")