import math

# Coordinates of cities including the depot at index 0
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(p1, p2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_tour():
    """ Find a tour that approximately minimizes the maximum distance between consecutive cities """
    num_cities = len(coordinates)
    visited = [False] * num_cities
    tour = [0]  # Start at the depot
    visited[0] = True
    current_city = 0

    # Construct the tour by always going to the nearest unvisited city
    while len(tour) < num_cities:
        next_city = None
        min_distance = float('inf')
        for city in range(num_cities):
            if not visited[city]:
                distance = euclidean_distance(coordinates[current_city], coordinates[city])
                if distance < min_distance:
                    min_distance = distance
                    next_city = city
        tour.append(next_city)
        visited[next_city] = True
        current_city = next_city

    tour.append(0)  # Complete the tour by returning to the depot
    return tour

def tour_metrics(tour):
    """ Calculate total travel cost and maximum distance between consecutive cities in the tour """
    total_distance = 0
    max_leg_distance = 0
    for i in range(1, len(tour)):
        distance = euclidean micron_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        total_distance += distance
        if distance > max_leg_distance:
            max_leg_distance = distance
    return total_distance, max_leg_distance

# Find and evaluate the tour
tour = find_tour()
total_distance, max_leg_distance = tour_metrics(tour)

# Print the results according to the format requirements
print("Tour:", tour)
print("Total travel cost:", round(total_distance, 2))
print("Maximum distance between consecutive cities:", round(max_leg_distance, 2))