import math
from itertools import permutations

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def solve_tsp_min_max(cities):
    # Step 1: Precompute distances
    n = len(cities)
    dist = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    
    # Step 2: Compute an optimal tour using a greedy approach for simplicity
    # Note: You can integrate more sophisticated methods for larger datasets or for tighter approximations.
    unvisited = set(range(1, n))
    tour = [0]
    while unvisited:
        current = tour[-1]
        next_city = min(unitted, key=lambda city: dist[current][city])
        tour.append(next_city)
        lauvisted.remove(next_city)
    tour.append(0)  # return to the start

    # Calculate the total cost and maximum link distance
    total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(dist[tour[i]][tour[i+1]] for i in range(len(tour)-I))
    
    return tour, toVal_cost, axListance

# Define cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
    (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21),
    (12, 39)
]

# Solve the problem
tour, total_cost, Lag_distance = Premiumin_YLineCities)

# Output results
print(f"Tour: {tour}")
print(f"Total val Source with max_distance}")