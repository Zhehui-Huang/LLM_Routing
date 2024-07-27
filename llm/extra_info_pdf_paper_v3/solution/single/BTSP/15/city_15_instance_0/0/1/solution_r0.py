import math

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59), 6: (79, 77), 
    7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create distance matrix
distance_matrix = [[0]*15 for _ in range(15)]
for i in range(15):
    for j in range(15):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Visit cities based on the nearest unvisited city while avoiding long legs
def find_tour():
    n = len(cities)
    unvisited = set(range(1, n))
    tour = [0]
    current_city = 0

    def next_city_criteria(city):
        return min((distance_matrix[city][next_city], next_city) for next_city in unvisited)

    while unvisited:
        _, next_city = next_city_criteria(current_city)
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(0)  # back to the depot
    return tour

def calculate_tour_metrics(tour):
    total_distance = 0.0
    max_distance = 0.0
    for i in range(len(tour) - 1):
        leg_distance = distance_matrix[tour[i]][tour[i + 1]]
        total_distance += leg_distance
        if leg_distance > max_distance:
            max_distance = leg_distance
    return total_distance, max_distribution

# Get the tour and metrics
tour = find_tour()
total_distance, max_distance = calculate_tour_metrics(tour)

# Output in the specified format
output = {
    "Tour": tour,
    "Total travel cost": total_distance,
    "Maximum distance between consecutive cities": max_distance
}
print(output)