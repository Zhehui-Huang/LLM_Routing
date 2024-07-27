import math
import itertools

# Define the city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generating all combinations of 7 cities (excluding the depot)
city_combinations = list(itertools.combinations(range(1, 10), 7))

# Function to calculate the total tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i+1])
    return total_cost

# Search for the shortest tour among possible city combinations
shortest_tour = None
shortest_cost = float('inf')

for combination in city_combations:
    # We have to include the depot city (0) in the tour
    potential_tour = [0] + list(combination) + [0]
    
    # Permutate over these cities to find the shortest path
    for perm in itertools.permutations(potential_tour[1:-1]):
        current_tour = [0] + list(perm) + [0]
        current_cost = calculate_tour_cost(current_tour)
    
        if current_cost < shortest_cost:
            shortest_cost = current_cost
            shortest_tour = current_tour

# Output the shortest tour found and its cost
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {shortest_cost}")