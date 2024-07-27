import itertools
from math import sqrt
import random

# Coordinates of cities: index 0 is the depot city
cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
          (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
          (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
          (64, 72), (14, 89)]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(route):
    """Calculate the total distance of the route."""
    dist = 0
    for i in range(len(route) - 1):
        dist += euclidean_distance(cities[route[i]], cities[route[i+1]])
    return dist

def nearest_neighbor_subset(start, cities_indices, k):
    """Create a route using the nearest neighbor heuristic considering a subset of cities."""
    route = [start]
    available = set(cities_indices) - {start}
    
    while len(route) < k:
        last = route[-1]
        next_city = min(available, key=lambda x: euclidean_distance(cities[last], cities[x]))
        route.append(next_city)
        available.remove(next_city)

    route.append(start)  # Complete the tour by returning to the depot
    return route

def select_random_subset_excluding_depot(total_cities, k, depot=0):
    """Select random k - 1 indices excluding the depot city."""
    return [depot] + random.sample([i for i in range(total_cities) if i != depot], k - 1)

def find_best_k_tsp(start, num_cities, k, trials=100):
    """Determine the best route visiting k cities using random subsets and nearest neighbor heuristic."""
    best_route = None
    best_cost = float('inf')
    
    for _ in range(trials):
        # Select random subset of cities including the depot
        subset = select_random_subset_excluding_depot(num_cities, k, start)
        
        # Generate a route by nearest neighbor approach within the subset
        candidate_route = nearest_neighbor_subset(start, subset, k)
        candidate_cost = total_distance(candidate_route)
        
        # Check if the found route is better
        if candidate_cost < best_cost:
            best_cost = candidate_cost
            best_route = candidate_route
    
    return best_route, best_cost

# Find the best route visiting exactly 16 cities starting and ending at city 0
best_route, best_cost = find_best_k_tsp(0, len(cities), 16)

print("Tour:", best_route)
print("Total travel cost:", best_cost)