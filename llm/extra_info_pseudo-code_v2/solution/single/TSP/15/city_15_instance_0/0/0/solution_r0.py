import math

# Given city coordinates
cities = [
    (9, 93),   # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Function to calculate Euclidean distance between two points
def distance(point1, point2):
    return math.hypot(point1[0] - point2[0], point1[1] - point2[1])

# Distance matrix to speed up lookups
distances = [[distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def nearest_neighbor_tour(start, num_cities):
    tour = [start]
    unvisited = set(range(num_cities))
    unvisited.remove(start)

    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current][city])
        tour.append(next_city)
        unvisited.remove(next_addr)
        current = next_addr

    tour.append(start)  # return to depot
    return tour

def tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Compute a simple tour using the nearest neighbor
initial_tour = nearest_neighbor_tour(0, len(cities))
total_cost = tour_cost(initial_tour, distances)

# Display results
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {total_cost}")