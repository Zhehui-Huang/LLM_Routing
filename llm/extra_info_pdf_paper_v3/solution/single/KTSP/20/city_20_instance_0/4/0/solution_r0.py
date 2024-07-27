import itertools
import math

# Define the coordinates of the cities
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Define a function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Find the shortest path that visits 4 cities including the depot
def find_shortest_route():
    min_cost = float('inf')
    best_route = []
    
    # Iterate over all combinations of 3 cities (not including the depot)
    for combination in itertools.combinations(range(1, 20), 3):
        # Create a route starting and ending at depot, including the 3 cities
        route = [0] + list(combination) + [0]
        
        # Find all permutations of the route visiting the cities exactly once
        for perm in itertools.permutations(route[1:-1]):
            current_route = [0] + list(perm) + [0]
            # Calculate the total distance of the current route
            current_cost = sum(distance(current_route[i], current_route[i+1]) for i in range(len(current_route) - 1))
            
            # If the current route has a lower cost than the minimum found so far, update
            if current_cost < min_cost:
                min_cost = current_cost
                best_route = current_route
    
    return best_route, min_cost

# Find the optimal tour and its cost
optimal_route, total_cost = find_shortest_route()

# Output the results
print("Tour:", optimal_route)
print("Total travel cost:", total_cost)