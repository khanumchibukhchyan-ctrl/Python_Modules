#!/usr/bin/env python3

import math

print("=== Game Coordinate System ===")

def get_player_pos() -> tuple:
	while True:
		try:
			coordinates = input("Enter new coordinates as floats in format 'x,y,z': ")
			values = coordinates.split(",")

			if len(values) != 3:
				print("Invalid syntax")
				continue

			x = float(values[0])
			y = float(values[1])
			z = float(values[2])

			return (x, y, z)
		except ValueError as e:
			print(e)

print("et a first set of coordinates")
first = get_player_pos()

print("Got a first touple: ", first)
print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")

distance = math.sqrt(first[0]**2 + first[1]**2 + first[2]**2)
print("Distance to center: ", round(distance, 4))

print("Got a second coordinates")
second = get_player_pos()

distance2 = math.sqrt((second[0] - first[0])**2 + (second[1] - first[1])**2 + (second[2] - first[2])**2)

print("Distance between the 2 sets of coordinates:", round(distance2, 4))
