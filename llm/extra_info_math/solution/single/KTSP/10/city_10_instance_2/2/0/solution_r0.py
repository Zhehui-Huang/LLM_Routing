import itertools
import math

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0]) ** 2 + (cities[city_a][1] - cities[city_b][1]) ** 2)

# Generating all combinations of 5 cities apart from the depot, to form a tour of 6 cities including the depot
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []
    
    # Iterate over all combinations of 5 cities (excluding depot)
    for combination in itertools.combinations(range(1, 10), 5):
        # Including depot city in the tour
        current_tour = [0] + list(combination) + [0]
        
        # Calculate the total travel cost of this tour
        current_cost = 0
        for i in range(len(current_tour) - 1):
            current_cost += euclidean_distance(current_tour[i], current_tour[i + 1])
        
        # Check if this is the minimal cost tour so far
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour
    
    return best_tour, min_cost

# Get the best tour and its cost
tour, cost = find_shortest_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))