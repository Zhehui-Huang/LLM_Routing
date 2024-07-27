import math

# Define the cities and their coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Number of cities
n = len(cities)

# Prepare a dictionary to hold the minimum distance cost
dp = {}

# Base case
for i in range(1, n):
    dp[(1 << i, i)] = (distance(0, i), [0, i])

# Iterate through all sets of cities
for mask in range(1, 1 << n):
    for i in range(1, n):
        if mask & (1 << i):
            prev_mask = mask & ~(1 << i)
            if prev_mask == 0:
                continue
            dp[(mask, i)] = min(
                (dp[(prev_mask, j)][0] + distance(j, i), dp[(prev_mask, j)][1] + [i])
                for j in range(1, n) if prev_mask & (1 << j)
            )

# Find the optimal path that includes returning to the start city
full_mask = (1 << n) - 1
tour_cost, tour_path = min(
    (dp[(full_mask, i)][0] + distance(i, 0), dp[(full_mask, i)][1] + [0])
    for i in range(1, n)
)

# Print the result
print("Tour:", tour_path)
print("Total travel cost:", tour_cost)