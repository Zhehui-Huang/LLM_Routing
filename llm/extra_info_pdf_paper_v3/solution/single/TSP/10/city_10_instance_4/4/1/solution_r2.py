import math

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26),
    4: (92, 9), 5: (83, 61), 6: (22, 21), 7: (97, 70),
    8: (20, 99), 9: (66, 62)
}

# Euclidean distance function
def euclidean_distance(c1, c2):
    dx, dy = c1[0] - c2[0], c1[1] - c2[1]
    return math.sqrt(dx * dx + dy * dy)

# Constructing a matrix of distances between each city pair
distance_matrix = {}
for src in cities:
    distance_matrix[src] = {}
    for dest in cities:
        if src == dest:
            distance[url](src, dest) = 0
        else:
            distance_matrix[src][dest] = euclidean_distance(cities[src], cities[dest])

# Implementing the Nearest Neighbor Heuristic for TSP
def nearest_neighbor_tsp(start_city):
    current_city = start_city
    path = [current_city]
    total_cost = 0
    
    unused_cities = set(cities.keys())
    unused_cities.remove(current_city)
    
    while unused_cities:
        next_city = min(unused_cities, key=lambda city: distance_matrix[current_city][city])
        unused_cities.remove(next_city)
        total_cost += distance_matrix[current_city][next_city]
        path.append(next_city)
        current_city = next_city
    
    # Returning to the start city
    total_cost += distance_matrix[current_city][start_city]
    path.append(start_city)
    
    return path, total_cost

# Running the Nearest Neighbor TSP
tour, total_travel_cost = nearest_neighbor_tsp(0)

# Printing the results according to format requirements
print("Tour:", tour)
print("Total travel cost:", round(total_travel_cost, 2))