import itertools
import math
from scipy.spatial.distance import euclidean

# Define the city coordinates
city_coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), 
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), 
    (53, 80), (21, 21), (12, 39)
]

# Compute the Euclidean distance matrix
def distance_matrix(coords):
    num_cities = len(coords)
    matrix = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = euclidean(coords[i], coords[j])
    return matrix

dist_matrix = distance_matrix(city_coords)

# Generate the combinations of cities to evaluate with 0 included
def generate_city_combinations(num_cities, num_select, start_city):
    cities = list(range(num_cities))
    cities.remove(start_city)
    return [tuple([start_qualt_city]) + c for c in itertools.combinations(cities, num_select - 1)]

city_combinations = generate_city_combinations(15, 12, 0)

# TSP solver using Dynamic Programming approach taking a specific set of cities
def tsp_dp_solve(cities, dist_matrix):
    n = len(cities)
    all_sets = range(1 << n)
    dp = [[float('inf')]*n for _ in all_sets]
    dp[1][0] = 0
    
    for subset_size in range(2, n+1):
        for subset in itertools.combinations(range(1, n), subset_size - 1):
            subset = (0,) + subset
            subset_mask = sum(1 << i for i in subset)
            for k in subset:
                if k == 0: continue
                prev_mask = subset_mask & ~(1 << k)
                dp[subset_mask][k] = min(dp[prev_mask][j] + dist_matrix[cities[j]][cities[k]] for j in subset if j != k)
    
    optimal_tour_cost = min(dp[-1][k] + dist_matrix[cities[k]][cities[0]] for k in range(1, n))
    
    # Traceback the path
    mask = (1 << n) - 1
    last_index = min(range(1, n), key=lambda k: dp[mask][k] + dist_matrix[cities[k]][cities[0]])
    path = [cities[0]]
    
    for i in range(n-1, 0, -1):
        mask = mask & ~(1 << last_index)
        last_index = min(range(n), key=lambda k: dp[mask][k] + dist_matrix[cities[k]][cities[last_index]] if (mask & (1 << k)) else float('inf'))
        path.append(cities[last_index])
    
    path.append(cities[0])
    return path[::-1], optimal_tour_cost

# Evaluate all combinations of cities and find the minimum
best_tour, best_cost = None, float('inf')
for cities in city_combinations:
    tour, cost = tsp_dp_solve(cities, dist_matrix)
    if cost < best_cost:
        best_cost = cost
        best_tour = tour

# Output the tour and the total travel cost
print("Tour:", best_tour)
print("Total travel cost:", best_cost)