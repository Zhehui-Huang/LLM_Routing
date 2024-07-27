import math

# City coordinates
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate all distances
num_cities = len(coordinates)
distances = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Nearest neighbor heuristic implementation
def nearest_neighbor_tour(start_city):
    unvisited = set(range(num_cities))
    tour = []
    current_city = start_city
    tour.append(current_city)
    unvisited.remove(current_city)
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        total_cost += distances[current_city][next_city]
        current_city = next_city
        tour.append(current_city)
        unvisited.remove(current
_city)

    # Return to the start city
    total_cost += distances[current_city][start_city]
    tour.append(start_city)
    return tour, total_cost

# Compute the tour from the depot city 0
tour, total_cost = nearest_neighbor_tour(0)

# Output the results as specified
print("Tour:", tour)
print("Total travel cost:", round(total_total cost))