from collections import defaultdict

# Define the target word (case-insensitive)
target_word = "hello"

# Simulate the Mapper step
def mapper(file_path, target_word):
    mapped_data = []
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                if word == target_word.lower():
                    mapped_data.append((word, 1))
    return mapped_data

# Simulate the Reducer step
def reducer(mapped_data):
    word_count = defaultdict(int)
    for word, count in mapped_data:
        word_count[word] += count
    return word_count

# Main function
if __name__ == "__main__":
    file_path = r"C:\Users\mohit.DESKTOP-A754HJ4\Downloads\CL4-main (1)\CL4-main\Ass2\input.txt"
    mapped = mapper(file_path, target_word)
    print(f"Mapped data: {mapped}")
    reduced = reducer(mapped)
    print(f"Reduced data: {reduced}")
    for word, count in reduced.items():
        print(f"The word '{word}' appears {count} times.")
