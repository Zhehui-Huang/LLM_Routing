import math
from itertools import permutations

# Coordinate setup for cities
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Groups of cities specified
city_groups = {
    0: [8, 12, 14],    # Group 0
    1: [7, 10, 11],    # Group 1
    2: [4, 6, 9],      # Group 2
    3: [1, 3, 13],     # Group 3
    4: [2, 5]          # Group 4
}

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Precompute all inter-city distances for efficiency
distances = {}
for c1 in cities:
    for c2 in cities:
        if c1 != c2:
            distances[(c1, c2)] = calculate_distance(c1, c2)

# Generate all possible selections of exactly one city from each group
def generate_city_combinations():
    from itertools import product
    return product(*city_groups.values())

# Compute the total cost of a complete tour
def calculate_tour_cost(tour):
    cost = distances[(0, tour[0])]  # start from depot
    for i in range(len(tour) - 1):
        cost += distances[(tour[i], tour[i + 1])]
    cost += distances[(tour[-1], 0)]  # return to depot
    return cost

# Find the shortest tour
def find_shortest_tour():
    shortest_tour = None
    shortest_cost = float('inf')
    for combination in generate_city_combinations():
        all_permutations = permutations(combination)
        for perm in all_permutations:
            tour_cost = calculate_tour_cost(perm)
            if tour_cost < shortest_cost:
                shortest_tour = perm
                shortest_cost = tour_cost
    
    # Include the depot in the final tour representation
    final_tour = [0] + list(shortest_tour) + [0]
    return final_tour, shortest_cost

# Compute the solution
tour, total_cost = find_shortest_tour()

# Print the outputs as required
print("Tour:", tour)
print("Total travel cost:", total_cost)