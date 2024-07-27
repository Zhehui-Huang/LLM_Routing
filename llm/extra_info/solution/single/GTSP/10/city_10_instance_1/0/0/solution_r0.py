import itertools
import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups of cities
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Function to calculate total route distance for a given tour
def total_route_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

# Brute-force approach to determine the shortest route
def find_shortest_route():
    min_distance = float('inf')
    best_route = None
    
    # Generate all product combinations of one city from each group
    for cities_per_group in itertools.product(*groups):
        # Create tour with start and end at depot
        current_tour = [0] + list(cities_per_group) + [0]
        
        # Calculate the route distance
        current_distance = total_route_distance(current_tour)
        
        # Check if current route is better than best found
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = current_tour
            
    return best_route, min_distance

# Run the function to find the best tour
tour, cost = find_shortest_route()

# Output the result in the specified format
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")