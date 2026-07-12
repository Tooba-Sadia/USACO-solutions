#Core drill DMOJ
import math  # We use math.pi to get the value of π


# Read the radius from input (integer)
r = int(input().strip())


# Read the height from input (integer)
h = int(input().strip())


# Use formula for the volume of a cone:
# V = (π * r^2 * h) / 3
volume = (math.pi * r * r * h) / 3


# Print the result
print(volume)
