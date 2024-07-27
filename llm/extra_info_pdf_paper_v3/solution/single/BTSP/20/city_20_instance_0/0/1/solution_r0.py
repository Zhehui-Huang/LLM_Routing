import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def solve_tsp_bottleneck(cities):
    # Calculate distances
    n = len(cities)
    dist = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    
    # Initial tour: start with a greedy algorithm
    unvisited = set(range(1, n))
    tour = [0]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: dist[last][x])
        tour.append(next_city)
        unvisited.remove(next_city)
    
    tour.append(0)  # return to the starting depot
    
    # Finding the maximum distance in the current tour configuration
    max_dist = max(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    # Total distance of the tour
    total_cost = sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    return tour, total_cost, max_dist

# Define cities' coordinates
cities = [
    (8, 11),   # Depot city 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Get tour result using our approximation strategy
tour_result, total_cost, max_distance = solve_tsp_bottleneck(cities)

# Display the results
print(f"Tour: {tour_result}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")