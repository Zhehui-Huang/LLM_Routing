import numpy as np
import itertools

# City coordinates, including the depot city
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate distances matrix
def calculate_distance(a, b):
    return np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

num_cities = len(coordinates)
distances = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distances[i, j] = calculate_distance(coordinates[i], coordinates[j])

def find_tour():
    # Trying different maximum bounds for the distances
    sorted_distances = np.sort(distances[np.triu_indices(num_cities, 1)])
    
    for d in sorted_distances:
        # Check if Hamiltonian cycle exists with max edge weight <= d
        graph = distances <= d
        for path in itertools.permutations(range(1, num_cities)):
            valid_path = True
            max_edge = 0
            last_city = 0
            total_cost = 0
            
            for city in path:
                if not graph[last_city, city]:
                    valid_path = False
                    break
                cost = distances[last_city, city]
                total_cost += cost
                max_edge = max(max_edge, cost)
                last_city = city
                
            if valid_path and graph[last_city, 0]:  # Check the return to the depot
                total_cost += distances[last_city, 0]
                max_edge = max(max_edge, distances[last_city, 0])
                return [0] + list(path) + [0], total_cost, max_edge
    
    return [], 0, 0  # In case no valid tour is found, though highly unlikely

tour, total_travel_cost, max_consecutive_distance = find_tour()
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_checkpoints)