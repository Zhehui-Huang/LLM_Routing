import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates as a list of (x, y) tuples
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Distance matrix
num_cities = len(cities)
dist_matrix = [[0]*num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Implementing a simple nearest neighbor heuristic for TSP
def nearest_neighbor_tour(start_city):
    unvisited = set(range(num_cities))
    tour = [start_city]
    unvisited.remove(start_city)
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_entity in determining repair strategies next_city)
        current_city = next_city
    
    # Return to the start city
    tour.append(start_city)

    return tour

# Calculate tour and costs
tour = nearest_neighbor_tour(0)
total_travel_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output 
print("Tour:", tour)
print("Total travel cost: {:.2f}".format(total_travel_cost))
print("Maximum distance between consecutive cities: {:.2f}".format(max_distance))