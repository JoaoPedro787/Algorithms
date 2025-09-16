# Linear vs Binary Search in a list of dictionaries
# Practice exercise from "Grokking Algorithms"

data = [
    {"name": "Ana", "phone": "1111-1111"},
    {"name": "Amanda", "phone": "2222-2222"},
    {"name": "André", "phone": "3333-3333"},
    {"name": "Beatriz", "phone": "4444-4444"},
    {"name": "Bruno", "phone": "5555-5555"},
    {"name": "Carlos", "phone": "6666-6666"},
    {"name": "Daniel", "phone": "7777-7777"},
    {"name": "Eduardo", "phone": "8888-8888"},
    {"name": "Fernanda", "phone": "9999-9999"},
    {"name": "Gabriel", "phone": "1010-1010"},
    {"name": "Helena", "phone": "1112-1112"},
    {"name": "Igor", "phone": "1212-1212"},
    {"name": "João", "phone": "1313-1313"},
    {"name": "Lucas", "phone": "1414-1414"},
    {"name": "Mariana", "phone": "1515-1515"},
    {"name": "Natália", "phone": "1616-1616"},
    {"name": "Otávio", "phone": "1717-1717"},
    {"name": "Paula", "phone": "1818-1818"},
    {"name": "Roberto", "phone": "1919-1919"},
    {"name": "Vinícius", "phone": "2020-2020"},
]

# Linear search - O(n)
linear_attempts = 0
for person in data:
    linear_attempts += 1
    if person["name"][0] == "E":
        print(f"Name: {person['name']} | Phone: {person['phone']}")

print(f"Linear search attempts: {linear_attempts}")
print("---------------------")


# Binary search - O(log n)
def binary_search():
    """Search for a name starting with 'E' using binary search."""
    attempts = 0
    low = 0
    high = len(data) - 1
    target = "E"

    while low <= high:
        attempts += 1
        mid = (low + high) // 2
        first_char = data[mid]["name"][0]

        if first_char > target:
            high = mid - 1
        elif first_char < target:
            low = mid + 1
        else:
            # Found a name starting with 'E'
            high = mid - 1  # Continue searching for earlier matches

    print(f"Name: {data[mid]['name']} | Phone: {data[mid]['phone']}")
    print(f"Binary search attempts: {attempts}")


binary_search()
