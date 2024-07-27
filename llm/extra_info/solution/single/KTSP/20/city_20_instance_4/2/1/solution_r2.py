import math

def euclidean_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_distance(tour, coordinates):
    """Calculate the total distance of a given tour."""
    total_distance = 0
    for i in range(1, len(tour)):
        city1 = coordinates[tour[i-1]]
        city2 = coordinates[tour[i]]
        total_distance += euclidean_distance(city1[0], city1[1], city2[0], city2[1])
    return total_distance

def nearest_neighbor(coordinates, total_cities):
    """Create an initial path using the nearest neighbor algorithm."""
    start = 0
    unvisited = list(range(1, len(coordinates)))
    path = [start]
    
    while len(path) < total_cities:
        last = path[-1]
        next_city = min(unvisited, key=lambda city: euclidean_distance(coordinates[last][0], coordinates[last][1], coordinates[city][0], coordinates[city][1]))
        path.append(next_city)
        unvisited.remove(next_city)
    
    path.append(start)  # return to the starting city
    return path

# Coordinates of each city, where index is the city index
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0),
    (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Find the tour using the nearest neighbor heuristic
tour = nearest_neighbor(coordinates, 16)

# Calculate the total travel distance of the found tour
total_travel_distance = calculate_total_distance(tour, coordinates)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_distance:.2f}")