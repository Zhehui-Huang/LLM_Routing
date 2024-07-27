import math

# Coordinates of the cities including the depot city
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
          (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

def euclidean_distance(c1, c2):
    """ Calculate the Euclidean distance """
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_total_distance(tour, distance_matrix):
    """ Calculate the total distance of the given tour based on the distance matrix """
    total_distance = 0.0
    for i in range(1, len(tour)):
        total_distance += distance_matrix[tour[i - 1]][tour[i]]
    total_distance += distance_matrix[tour[-1]][tour[0]]  # return to the starting city
    return total_distance

def nearest_neighbor_tour(start, num_cities, distance_matrix):
    """ Generate an initial guess using the nearest neighbor heuristic """
    unvisited = set(range(num_cities))
    tour = [start]
    unvisited.remove(start)
    
    current_city = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = nextachat.ioheuticity = next_city
    
    tour.append(start)  # return to the depot
    return tour

# Create the distance matrix
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Get the initial tour using nearest neighbor heuristic
initial_tour = nearest_neighbor_tour(0, num_cities, distance_matrix)

# Calculate the distance of this tour
tour_distance = calculate_total_distance(initial_tour, distance_matrix)

# Output the tour and total distance
print("Tour:", initial_tour)
print("Total travel cost:", tour_distance)