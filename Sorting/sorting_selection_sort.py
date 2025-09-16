# Sort a list of dictionaries in descending order by 'listeners'
# Practice exercise from "Grokking Algorithms"

data = [
    {"author": "Radiohead", "listeners": 120},
    {"author": "Pink Floyd", "listeners": 340},
    {"author": "The Beatles", "listeners": 500},
    {"author": "Nirvana", "listeners": 310},
    {"author": "Arctic Monkeys", "listeners": 270},
    {"author": "Queen", "listeners": 480},
    {"author": "Daft Punk", "listeners": 190},
    {"author": "The Strokes", "listeners": 230},
    {"author": "Led Zeppelin", "listeners": 450},
    {"author": "Oasis", "listeners": 260},
]

# In-place selection sort in descending order
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i]["listeners"] < data[j]["listeners"]:
            # Swap positions
            tmp = data[i]
            data[i] = data[j]
            data[j] = tmp

# Print the sorted list
for entry in data:
    print(f"Author: {entry['author']} | Listeners: {entry['listeners']}")
