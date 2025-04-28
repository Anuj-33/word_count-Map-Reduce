# full_pipeline.py

def map_phase(lines):
    mapped = []
    for line in lines:
        words = line.strip().split()
        for word in words:
            mapped.append((word.lower(), 1))
    return mapped

def shuffle_phase(mapped):
    shuffled = {}
    for word, count in mapped:
        if word in shuffled:
            shuffled[word].append(count)
        else:
            shuffled[word] = [count]
    return shuffled

def reduce_phase(shuffled):
    reduced = {}
    for word, counts in shuffled.items():
        reduced[word] = sum(counts)
    return reduced

# MAIN
if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    mapped = map_phase(lines)
    shuffled = shuffle_phase(mapped)
    reduced = reduce_phase(shuffled)

    for word, total_count in reduced.items():
        print(f"{word}: {total_count}")
