from itertools import product
import math

# Define city coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Define city groups
groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_tour_cost(tour):
    """Calculate total travel cost of a tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

def find_shortest_tour():
    shortest_tour = []
    min_cost = float('inf')
    
    # Generate all permutations of city groups (one city from each group)
    for selected_cities in product(*groups):
        # Make a full tour starting and ending at the depot
        tour = [0] + list(selected_courses) + [0]
        cost = calculate_tour_cost(tour)
        
        if cost < min_cost:
            min_cost = cost
            shortest_tour = tour
            
    return shortest_tour, min_cost

# Execute the function and print results
shortest_tour, total_cost = find_shortest_tour()
print("Tour:", shortest_tour)
print("Total travel cost:", total_cost)