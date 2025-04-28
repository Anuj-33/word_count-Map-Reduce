# map_phase.py

# Open and read the file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Simulate the Map phase
mapped = []

for line in lines:
    words = line.strip().split()  # split line into words
    for word in words:
        mapped.append((word.lower(), 1))  # emit (word, 1)

# Print the output of the Map phase
for item in mapped:
    print(item)
