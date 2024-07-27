import itertools
import math

# City coordinates with indices corresponding to city numbers
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

# City groups
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of cities taking one from each group
city_combinations = list(itertools.product(*city_group))

# Function to calculate the total travel cost of a tour starting and ending at depot
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Find the shortest route
def find_shortest_route():
    best_tour = None
    best_cost = float('inf')
    
    for combination in city_combinations:
        # Form a tour starting and ending at the depot (0)
        tour = [0] + list(combination) + [0]
        
        # Calculate cost of this tour
        tour_cost = calculate_tour_cost(tour)
        
        # Update the best tour found
        if tour_cost < best_cost:
            best_cost = tour_cost
            best_tour = tour
            
    return best_tour, best_cost

# Obtain the best route and its cost
shortest_tour, shortest_cost = find_shortest_route()

# Print the solution
print("Tour:", shortest_tour)
print("Total travel cost:", shortest_cost)