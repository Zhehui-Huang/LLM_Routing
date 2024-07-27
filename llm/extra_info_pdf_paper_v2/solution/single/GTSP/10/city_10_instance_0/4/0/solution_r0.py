import math
import itertools

# Coordinates of each city where index corresponds to city number
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

# Grouping of cities
groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all tours that visit one city from each group and start/end at the depot
def generate_tours():
    for comb in itertools.product(*groups):
        yield (0,) + comb + (0,)

# Find the shortest tour
def find_best_tour():
    best_tour = None
    min_cost = float('inf')
    
    for tour in generate_tours():
        cost = sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
            
    return best_tour, min_cost

best_tour, total_cost = find_best_tour()

# Output the best tour and the total travel cost
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {total_cost:.2f}")