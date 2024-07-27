import math
import itertools

# City coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find shortest path visiting exactly n cities starting and ending at the depot
def find_shortest_path(depot, num_cities):
    all_routes = list(itertools.combinations(range(1, len(cities)), num_cities - 1))
    best_distance = float('inf')
    best_route = None
    
    # Evaluate all possible combinations of cities
    for route in all_routes:
        full_route = [depot] + list(route) + [depot]
        # Calculate total distance
        distance = sum(euclidean_distance(full_route[i], full_route[i+1]) for i in range(len(full_route) - 1))
        
        if distance < best_distance:
            best_distance = distance
            best_route = full_route
            
    return best_route, best_distance

# Finding the shortest path visiting 10 cities
best_route, best_distance = find_shortest_path(0, 10)

# Output results
print("Tour:", best_route)
print("Total travel cost:", round(best_distance, 2))