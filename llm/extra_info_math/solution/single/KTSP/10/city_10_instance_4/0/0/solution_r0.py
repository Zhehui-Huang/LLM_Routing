import math
from itertools import combinations

# City coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate distances matrix
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Greedy algorithm to find a short tour that visits exactly k cities including the depot
def find_shortest_tour(k):
    best_tour = []
    min_cost = float('inf')
    
    # Try all combinations of k-1 cities excluding the depot
    for comb in combinations(range(1, n), k-1):
        # Include the depot in the tour
        tour = [0] + list(comb) + [0]
        
        # Calculate the cost of this tour
        total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

        # Check if this tour is better than the previously found ones
        if total_cost < min_cost:
            best_tour = tour
            min_cost = total_cost
    
    return best_tour, min_cost

# We need to visit exactly 8 cities, starting and ending at the depot city 0
k = 8
tour, total_cost = find_shortest_tour(k)

# Returning output in the required format
output = f"Tour: {tour}\nTotal travel cost: {total_cost:.2f}"
print(output)