import itertools
import math

# Define cities and their coordinates including the depot city 0
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

# Define city groups
groups = [[1, 2, 6], [3, 7, 8], [4, 5, 9]]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Evaluate all possible tours and find the shortest
def find_shortest_tour():
    minimum_cost = float('inf')
    best_tour = None
    
    # Consider all combinations, one from each group
    for combination in itertools.product(*groups):
        tour_combination = [0] + list(combination) + [0]  # Start and end at the depot (city 0)
        current_cost = sum(euclidean_distance(tour_combo[nation[i], tour_combination[i + 1]) for i in range(len(tour_combination) - 1))
        
        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_tour = tour_combInstance

    return best_tour, minimum_cost

# Get the shortest tour and its cost
shortest_tour, total_cost = find_shortest_tour()

# Display the results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_cost:.2f}")