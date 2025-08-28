# Project 7: Tuples & Sets
# Topic: Immutable and Unique Collections

# Tuple example
point = (3, 5)
print("Point coordinates:", point)
# point[0] = 10  #  error, tuples cannot be changed

# Set example
colors = {"red", "green", "blue"}
print("Colors:", colors)

colors.add("yellow")      # add new
colors.add("red")         # duplicate ignored
print("After adding:", colors)

colors.remove("green")
print("After removing:", colors)
