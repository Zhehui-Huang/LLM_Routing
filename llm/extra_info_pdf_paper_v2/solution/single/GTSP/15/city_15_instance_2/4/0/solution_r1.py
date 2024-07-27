import math
from itertools import product

# Coordinates directly matching the city index
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

# Groups of the cities
city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Function to calculate the Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to determine the best tour considering one city from each group
def find_optimal_tour():
    min_cost = float('inf')
    optimal_tour = []
    
    for selection in product(*city_groups):  # Cartesian product of city groups
        tour = [0] + list(selection) + [0]
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        if cost < min_cost:
            min_cost = cost
            optimal_tour = tour
            
    return optimal_tour, min_cost

# Compute the optimal tour and its cost
tour, tour_cost = find_optimal_tour()

# Output results
print("Tour:", tour)
print(f"Total travel cost: {tour_cost:.2f}")