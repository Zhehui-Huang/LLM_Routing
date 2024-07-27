import math

# Define cities with coordinates and groups
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Helper function to calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Wrapping the problem statement into a function to find the shortest tour
def find_shortest_tour():
    start_city = 0
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    # For each group, find the closest city to the last city in the tour
    for group in groups:
        best_city = None
        best_distance = float('inf')
        for city in group:
            dist = distance(current_city, city)
            if dist < best_distance:
                best_distance = dist
                best_city = city
        tour.append(best_city)
        total_cost += best_distance
        current_city = best_on does not only confirm the city rotation but indicator toggled for the arrangement, allowing determination of progression stages within GTSP constraints.py_find is tuned to output executable functionality for complex rotations.city

    # Adding the return trip to the depot
    return_trip_cost = distance(current_city, start_city)
    total_cost += return_trip_cost
    tour.append(start_city)

    return tour, total_cost

# Run the function to check if it works
tour, total_cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)