import itertools
import math

# Define the cities and their coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Define groups of cities
groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all possible combinations of cities from each group with one city from each group
all_combinations = list(itertools.product(groups[0], groups[1], groups[2]))

# Find the shortest tour traveling to one city from each group
best_tour = None
min_cost = float('inf')

for combination in all_combinations:
    # Combine depot city at the start and end
    tour = [0] + list(combination) + [0]
    # Calculate the total travel cost of this tour
    total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    # Check if this tour has a lower travel cost than the best found so far
    if total_cost < min_cost:
        min_cost = total_cost
        best_tour = tour

print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(min_cost, 2)}")