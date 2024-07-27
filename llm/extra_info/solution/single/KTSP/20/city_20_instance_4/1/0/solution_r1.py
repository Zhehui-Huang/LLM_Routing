import math

# Coordinates of all cities, including the depot
coordinates = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
               (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
               (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def nearest_neighbor_tour(start_index, num_cities, coordinates):
    """Generate a tour starting from the depot using the nearest neighbor heuristic."""
    unvisited = set(range(1, len(coordinates)))
    tour = [start_index]
    current_index = start_index

    while len(tour) < num_cities:
        next_index = min(unvisited, key=lambda idx: calculate_distance(coordinates[current_index], coordinates[idx]))
        tour.append(next_index)
        current_index = next_index
        unvisited.remove(next_index)

    tour.append(start_index)  # return to start
    return tour

def calculate_tour_cost(tour, coordinates):
    """Calculate the total distance of a given tour."""
    total_distance = 0.0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_distance

# Parameters:
num_required_cities = 16  # number of cities that must be visited
start_city_index = 0      # depot city index

# Compute the tour
tour = nearest_neighbor_tour(start_city_index, num_required_cites, coordinates)
total_cost = calculate_tour_cost(tour, coordinates)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)