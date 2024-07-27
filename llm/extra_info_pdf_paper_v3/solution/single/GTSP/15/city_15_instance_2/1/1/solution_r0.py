import math

# City coordinates
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
    14: (6, 99)
}

# Groups of cities
groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Find the closest city in each group to the depot
def find_closest_to_depot():
    representatives = {}
    for group_id, city_list in groups.items():
        closest_city = min(city_list, key=lambda x: euclidean_distance(0, x))
        representatives[group_id] = closest_city
    return representatives

# Calculate the minimum tour using the nearest neighbor heuristic
def nearest_neighbor_tsp(start_city, city_list):
    unvisited = city_list[:]
    current_city = start_city
    tour = [current_city]
    total_distance = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(current_city, x))
        distance_to_next = euclidean_distance(current_city, next_city)
        total_distance += distance_to_next
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    # Return to the depot
    total_distance += euclidean_distance(current_city, start_city)
    tour.append(start_city)
    return tour, total_distance

# Main solving function
def solve_gtsp():
    representatives = find_closest_to_depot()  # Closest city from each group
    selected_cities = [0] + [rep for rep in representatives.values()]  # Depot + selected representatives
    tour, total_cost = nearest_neighbor_tsp(0, selected_cities)
    return tour, total_cost

# Get the results
tour, total_cost = solve_gtsp()
print("Tour:", tour)
print("Total travel cost:", total_cost)