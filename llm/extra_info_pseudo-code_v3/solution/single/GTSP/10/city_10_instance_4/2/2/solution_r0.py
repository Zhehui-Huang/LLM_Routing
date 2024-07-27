from itertools import product
from math import sqrt

# Define the cities and their coordinates, city index as the key
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

# Define the groups of cities
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def find_shortest_tour():
    # Create all combinations of cities, selecting one city from each group
    all_combinations = list(product(*city_groups))
    
    # Initialize minimum distance to a large number
    min_distance = float('inf')
    best_tour = None
    
    # Evaluate each combination
    for combination in all_combinations:
        # Add the depot city to the start and end
        tour = [0] + list(combination) + [0]
        # Calculate the tour distance
        tour_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Update the best tour found
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = tour
    
    return best_tour, min_distance

# Get the result
tour, total_distance = find_shortest_tour()

# Format the output
print("Tour:", tour)
print("Total travel cost:", round(total_distance, 2))