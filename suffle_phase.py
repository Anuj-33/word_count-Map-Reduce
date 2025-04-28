# shuffle_phase.py

# Open and read the file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Map Phase
mapped = []
for line in lines:
    words = line.strip().split()
    for word in words:
        mapped.append((word.lower(), 1))

# Shuffle Phase
shuffled = {}

for word, count in mapped:
    if word in shuffled:
        shuffled[word].append(count)
    else:
        shuffled[word] = [count]

# Print the output of Shuffle Phase
for word, counts in shuffled.items():
    print(f"{word}: {counts}")
