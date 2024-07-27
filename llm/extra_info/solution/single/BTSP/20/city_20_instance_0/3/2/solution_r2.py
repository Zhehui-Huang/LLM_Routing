import math

# City coordinates list
cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
          (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
          (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
          (60, 63), (93, 15)]

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Construct distance matrix
num_cities = len(cities)
distances = [
    [euclidean_distance(cities[i], cities[j]) for j in range(num_cities)]
    for i in range(num_cities)
]

# Find solution using nearest neighbor heuristic
def nearest_neighbor(start_city):
    unvisited = list(range(num_cities))
    tour = [start_city]
    unvisited.remove(start_city)
    
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current_city][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # returning to the depot
    return tour

# Compute the tour using nearest neighbor starting from the depot (city 0)
tour = nearest_neighbor(0)

# Calculate total travel cost and the maximum distance between consecutive cities
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output results:
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")