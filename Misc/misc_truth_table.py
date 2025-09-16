# A | B | NOT A | NOT B | A AND B | A OR B | A XOR B
# --|---|-------|-------|---------|--------|--------
# 0 | 0 |   1   |   1   |    0    |   0    |   0
# 0 | 1 |   1   |   0   |    0    |   1    |   1
# 1 | 0 |   0   |   1   |    0    |   1    |   1
# 1 | 1 |   0   |   0   |    1    |   1    |   0


# Generate a truth table for N variables
# Practice exercise from "Grokking Algorithms"

import string

alphabet = string.ascii_uppercase

num_vars = 2  # Number of variables

total_rows = 2**num_vars  # Total combinations for the truth table

# Generate the truth table
truth_table = [
    {
        "row": [
            {
                "var": alphabet[l],
                "value": True if (x // 2**l) % 2 == 1 else False,
            }
            for l in range(num_vars)
        ]
    }
    for x in range(total_rows)
]

# Print the truth table
for i, row_data in enumerate(truth_table):
    print(f"Row {i + 1}: {row_data['row']}")
