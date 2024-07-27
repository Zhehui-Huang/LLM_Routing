from itertools import permutations, combinations
import math

# Given cities and their coordinates
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

# Function to calculate euclidean distance
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to compute the cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance(cities[tour[i-1]], cities[tour[i]])
    total_cost += distance(cities[tour[-1]], cities[tour[0]])  # Back to depot
    return total_cost

# Function to find the shortest tour that visits 7 cities (including the depot)
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = None

    # Generate all combinations of 6 other cities
    for comb in combinations(range(1, 20), 6):
        current_cities = [0] + list(comb)  # Include the depot
        # Generate permutations of the current cities + back to depot
        for perm in permutations(current_cities):
            if perm[0] == 0:  # Ensure tour starts at the depot
                cost = tour_cost(perm)
                if cost < min_cost:
                    min_cost = cost
                    best_tour = perm
    
    return best_tour, min_cost

# Get the optimal tour and its cost
optimal_tour, total_cost = find_shortest_tour()

# Output the results
print(f"Tour: {list(optimal_tour)}")
print(f"Total travel cost: {total_cost}")