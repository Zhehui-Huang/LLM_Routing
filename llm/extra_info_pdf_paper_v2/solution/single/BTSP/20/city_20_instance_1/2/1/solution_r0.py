import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# City coordinates indexed by city numbers
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a matrix of distances
num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
                   for i in range(num_cities)]

# Find a minimum spanning tree (MST)
mst_matrix = minimum_spanning_tree(csr_matrix(distance_matrix)).toarray()

def find_tour(mst_matrix):
    # Simple MST-based approach for TSP
    visited = [False] * num_cities
    tour = [0]
    visited[0] = True
    
    while len(tour) < num_cities:
        last = tour[-1]
        next_city = min((mst_matrix[last][j], j) for j in range(num_cities) if not visited[j])[1]
        tour.append(next_city)
        visited[next_city] = True
    
    # Return to the starting point (depot)
    tour.append(0)
    return tour

def calculate_costs_distance(tour):
    total_cost = 0
    max_distance = 0
    
    for i in range(len(tour) - 1):
        dist = distance_matrix[tour[i]][tour[i+1]]
        total_cost += dist
        max_distance = max(max_distance, dist)
    
    return tour, total_cost, max_distance

# Get the tour
tour = find_tour(mst_matrix)

# Calculate the total travel cost and maximum distance between consecutive cities
final_tour, total_cost, max_distance = calculate_costs_distance(tour)

# Printing the required outputs
print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")