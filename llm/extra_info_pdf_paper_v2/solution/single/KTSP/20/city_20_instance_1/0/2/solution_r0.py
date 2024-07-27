import math
from itertools import combinations

# Coordinates of the cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Calculate the total tour cost
def tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all combinations of 6 cities (excluding the depot)
city_combinations = combinations([i for i in range(1, 20)], 6)

# Find the optimal tour
best_tour = None
min_cost = float('inf')

for comb in city_combinations:
    # Create possible tours by appending the depot city 0 at start and end
    possible_tour = [0] + list(comb) + [0]

    # Check all permutations of the 6 cities to find the minimum tour cost
    for perm in permutations(possible_tour[1:-1]):
        current_tour = [0] + list(perm) + [0]
        current_cost = tour_cost(current_tour)
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")