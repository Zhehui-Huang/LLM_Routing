import math
from itertools import product

# Define cities and their coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Define city groups
city_groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all possible tours
def generate_possible_tours():
    all_tours = []
    all_combinations = product(*city_groups.values())
    
    for comb in all_combinations:
        tour = [0] + list(comb) + [0]  # Start and end at the depot city
        total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        all_tours.append((tour, total_cost))
    
    return all_tours

# Find the tour with the minimum cost
def find_min_cost_tour():
    possible_tours = generate_possible_tours()
    min_tour = min(possible_tours, key=lambda x: x[1])
    return min_tour

# Execute the solution method
optimal_tour = find_min_cost_tour()

# Output the optimal tour and its total travel cost
print(f"Tour: {optimal_tour[0]}")
print(f"Total travel cost: {optimal_tour[1]:.2f}")