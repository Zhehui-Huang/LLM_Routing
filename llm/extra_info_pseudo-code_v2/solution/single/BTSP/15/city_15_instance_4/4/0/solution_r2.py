import math
import itertools

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def tsp_tour(cities):
    # Calculate all pairwise distances
    n = len(cities)
    dist = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    
    # All permutations of city indices, skip the first city as a fixed start
    min_tour = None
    min_max_dist = float('inf')
    total_min_cost = float('inf')
    
    for perm in itertools.permutations(range(1, n)):
        tour = [0] + list(perm) + [0]  # start and end at the depot city 0
        max_dist = max(dist[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        # Check if this tour has a smaller maximum distance between consecutive cities
        if max_dist < min_max_dist or (max_dist == min_max_dist and total_cost < total_min_cost):
            min_tour = tour
            min_max_dist = max_dist
            total_min_cost = total_cost

    return min_tour, total_min_cost, min_max_dist

# Define city coordinates
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), (97, 62),
          (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Solve the problem
tour, total_cost, max_distance = tsp_tour(cities)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")