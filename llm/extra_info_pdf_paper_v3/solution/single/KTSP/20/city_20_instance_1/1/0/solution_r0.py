import math
import random

# Define the cities and their coordinates
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
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to calculate the total tour cost
def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Multi-start heuristic function to find the shortest tour visiting exactly 7 cities
def find_shortest_tour(num_cities=7, attempts=1000):
    best_tour = None
    best_cost = float('inf')
    all_cities = list(cities.keys())[1:]  # Excluding the depot city from the choices
    
    for _ in range(attempts):
        # Randomly pick 6 cities plus the depot to make a group of 7 cities (The depot is always included)
        chosen_cities = random.sample(all_cities, num_cities-1)
        chosen_cities = [0] + chosen_cities  # Adding the depot

        # Generate all permutations of the chosen set
        for perm in permutations(chosen_cities):
            # Make sure the tour starts and ends at the depot
            if perm[0] == 0:
                current_tour = list(perm) + [0]  # Adding the depot to end the tour
                current_cost = tour_cost(current_tour)
                
                # Check if the found tour is better (cost-wise) than the best found so far
                if current_cost < best_cost:
                    best_tour = current_tour
                    best_cost = current_cost

    return best_tour, best_cost

# Function that generates permutations (used in generating possible tours)
def permutations(elements):
    if len(elements) == 1:
        yield elements
    else:
        for perm in permutations(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

# Find and print the best tour and its cost
best_tour, best_cost = find_shortest_tour()
print("Tour:", best_turlst_tour)
print("Total travel cost:", round(best_cost, 2))