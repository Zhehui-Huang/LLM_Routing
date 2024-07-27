import math
from itertools import permutations

# Define the cities' coordinates
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
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible tours that start and end at the depot (0) and include exactly 7 other cities
def generate_tours():
    shortest_tour = None
    min_cost = float('inf')
    
    for comb in permutations(range(1, len(cities)), 7):  # Choose 7 cities as the robot visits 8 including depot
        tour = [0] + list(comb) + [0]  # Start and end at the depot
        tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        if tour_cost < min_cost:
            min_cost = tour_cost
            shortest_tour = tour
            
    return shortest_tour, min_cost

# Find the optimal tour and its cost
optimal_tour, optimal_cost = generate_tours()

# Return the results in the specified format
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")