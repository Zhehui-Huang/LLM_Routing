import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to calculate the Euclidean distance between two cities
def distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Find the shortest tour that visits all cities, starting and ending at city 0
def find_shortest_tour():
    non_depot_cities = list(cities.keys())[1:]  # Exclude the depot city for permutations
    best_tour = None
    min_cost = float('inf')
    
    # Iterate over all permutations of the non-depot cities
    for perm in permutations(non_depot_cities):
        # Construct the complete tour starting and ending at the depot city
        tour = [0] + list(perm) + [0]
        # Calculate the total cost of this tour
        total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

        # If the calculated cost is lower than the current minimum, update the best tour and cost
        if total_cost < min_cost:
            min_cost = total_cost
            best_tour = tour

    return best_tour, min_cost

# Compute the best tour and its cost
best_tour, tour_cost = find_shortest_tour()

# Output the shortest tour and the corresponding travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {tour_cost:.2f}")