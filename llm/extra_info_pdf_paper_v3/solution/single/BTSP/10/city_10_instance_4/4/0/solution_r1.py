import math

# Coordinates of each city, including the depot
city_locations = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

def euclidean_distance(city1, city2):
    # Calculate the Euclidean distance between two cities given their coordinates
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Distance matrix initialization
n = len(city_locations)
distance_matrix = [[0]*n for _ in range(n)]

# Compute distance between all pairs of cities
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(city_locations[i], city_locations[j])

# Nearest Neighbor algorithm to provide a simple heuristic tour
def nearest_neighbor(start=0):
    unvisited = set(range(n))
    tour = []
    current = start
    
    while unvisited:
        tour.append(current)
        unvisited.remove(current)
        if unvisited:  # find minimal distance city
            next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
            current = next_city  # This fixes incorrect var reference
    
    tour.append(start)  # return to the depot
    return tour

tour = nearest_neighbor()

# Calculate total travel cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0

for i in range(1, len(tour)):
    dist = distance_matrix[tour[i-1]][tour[i]]
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Output the results formatted as specified
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive and the reactions: {max_distance:.2f}")