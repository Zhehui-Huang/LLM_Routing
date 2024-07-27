import itertools
import math

# Define the cities and their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance between two cities given their indices
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to calculate the total path cost
def total_cost(path):
    return sum(distance(path[i], path[i+1]) for i in range(len(path) - 1))

# Number of selected cities including the depot city
k = 7

# Generate all combinations of selecting k-1 cities excluding the depot
city_combinations = itertools.combinations([i for i in cities if i != 0], k - 1)

# Find the shortest path for visiting exactly k cities starting and ending at the depot
min_cost = float('inf')
best_path = []

for combination in city_combinations:
    selected_cities = (0,) + combination  # include depot city
    # Generate all possible permutations of the selected cities
    permutations = itertools.permutations(selected_cities)
    for perm in permutations:
        if perm[0] == 0 and perm[-1] == 0:  # start and end at depot
            cost = total_cost(perm)
            if cost < min_cost:
                min_cost = cost
                best_path = list(perm)

# Print the best path and its cost
print(f"Tour: {best_path}")
print(f"Total travel cost: {min_cost:.2f}")