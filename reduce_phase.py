# reduce_phase.py

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

# Reduce Phase
reduced = {}
for word, counts in shuffled.items():
    reduced[word] = sum(counts)

# Print the final output
for word, total_count in reduced.items():
    print(f"{word}: {total_count}")
