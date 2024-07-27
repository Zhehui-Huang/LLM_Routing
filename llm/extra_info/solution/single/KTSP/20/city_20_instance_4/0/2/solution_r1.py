import itertools
from scipy.spatial.distance import euclidean
from math import inf

# City coordinates indexed by city number (0-19)
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to compute Euclidean distances between all pairs of cities
def compute_distances(coords):
    n = len(coords)
    dists = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dists[i][j] = euclidean(coords[i], coords[j])
            else:
                dists[i][j] = inf
    return dists

distances = compute_distances(coordinates)

# Solving the constrained TSP
def find_min_tour(start_city, num_cities):
    cities = list(range(1, 20))  # we exclude the depot initially for permutations
    shortest_tour = None
    min_cost = inf
    
    for chosen_cities in itertools.combinations(cities, num_cities-1):  # Choose 15 cities as we already include the depot
        full_tour = [start_city] + list(chosen_cities) + [start_city]  # Complete tour starting and ending at the depot
        all_tours = itertools.permutations(full_tour[1:-1])  # Permute intermediate cities only
        
        for tour in all_tours:
            tour = [start_city] + list(tour) + [start_city]
            cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            
            if cost < min_cost:
                min_cost = cost
                shortest_tour = tour
            
    return shortest_tour, min_cost

tour, total_cost = find_min_tour(0, 16)

print("Tour:", tour)
print("Total travel cost:", total_cost)