import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def make_tour_from_mst(num_cities, mst):
    visited = np.zeros(num_cities, dtype=bool)
    tour = []
    stack = [0]
    
    while stack:
        city = stack.pop()
        if not visited[city]:
            visited[city] = True
            tour.append(city)
            # Find all cities connected to the current city in the MST
            for neighbor in range(num_cities):
                if mst[city, neighbor] > 0 and not visited[neighbor]:
                    stack.append(neighbor)
                    
    return tour + [0]  # Returning back to depot

# Coordinates of cities including depot
coordinates = np.array([
    (79, 15),  # Depot City 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
])

# Calculate the Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Compute the MST
mst_matrix = minimum_spanning_tree(dist_matrix).toarray()

# Create tour from MST
tour = make_tour_from_mst(len(coordinates), mst_matrix)

# Calculate the total travel cost and the maximum distance between any two consecutive cities
tour_costs = [euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1)]
total_travel_cost = sum(tour_costs)
max_travel_cost = max(tour_costs)

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_travel_cost)