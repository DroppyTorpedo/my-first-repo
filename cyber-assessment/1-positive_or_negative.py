#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
	print(f"{number} positive")
else number < 0:
	print(f"{number} negative")
else number == 0:
	print(f"{number} zero")
else:
	print(f"wrong type")