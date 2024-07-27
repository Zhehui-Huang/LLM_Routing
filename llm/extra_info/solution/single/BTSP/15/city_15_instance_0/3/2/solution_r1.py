import math

# Define the coordinates of the cities
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(coord1, coord2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def find_tour(cities):
    N = len(cities)
    unvisited = set(cities.keys())
    tour = [0]  # start at the depot city 0
    unvisited.remove(0)
    current_city = 0

    # Visit the rest of the cities to minimize the maximum distance
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    tour.append(0)  # end at the depot city 0
    return tour

def calculate_tour_cost(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

# Calculate the tour
tour = find_tour(cities)

# Calculate cost and maximum distance of the tour.
total_cost, max_distance = calculate_tour_cost(tour)

# Output the results
print("Tour:", tour)
print("Total travel our cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))