import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates (including depots)
coordinates = [
    (30, 40), (37, 52),  # Depot 0, Depot 1
    (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distances between all pairs of cities
num_cities = len(coordinates)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean(coordinates[i], coordinates[j])
        else:
            distances[i][j] = float('inf')

def get_min_tour():
    min_cost = float('inf')
    best_tour_0, best_tour_1 = [], []
    
    # Permute through arrangements of cities excluding depots
    cities_to_visit = list(range(2, num_cities))  # City indices excluding depots
    for partition in permutations(cities_to_visit):
        for split_point in range(1, len(partition)):
            tour_0 = [0] + list(partition[:split_point]) + [0]
            tour_1 = [1] + list(partition[split_point:]) + [1]
            
            cost_0 = sum(distances[tour_0[i]][tour_0[i+1]] for i in range(len(tour_0)-1))
            cost_1 = sum(distances[tour_1[i]][tour_1[i+1]] for i in range(len(tour_1)-1))
            total_cost = cost_0 + cost_1
            
            if total_cost < min_cost:
                min_cost = total_cost
                best_tour_0, best_tour_1 = tour_0, tour_1
    
    return best_tour_0, best_tour_1, min_cost

# Execute the function to find the optimal solution
best_tour_0, best_tour_1, total_min_cost = get_min_tour()

# Individual travel costs
cost_tour_0 = sum(distances[best_tour_0[i]][best_tour_0[i+1]] for i in range(len(best_tour_0)-1))
cost_tour_1 = sum(distances[best_tour_1[i]][best_tour_1[i+1]] for i in range(len(best_tour_1)-1))

# Output results
print("Robot 0 Tour:", best_tour_0)
print("Robot 0 Total Travel Cost:", cost_tour_0)
print("Robot 1 Tour:", best_tour_1)
print("Robot 1 Total Travel Cost:", cost_tour_1)
print("Overall Total Travel Cost:", total_min_cost)