import math

# Define the cities coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Calculate all distances between cities
num_cities = len(cities)
distances = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i < j:
            dist = euclidean_distance(i, j)
            distances[(i, j)] = dist
            distances[(j, i)] = dist

# Helper function to find the city with the min max edge cost to add to the tour
def find_min_max_edge_city(current_city, unvisited):
    min_max_dist = float('inf')
    next_city = None
    for city in unvisited:
        max_dist_for_city = max(euclidean_distance(current_city, city),
                                max([euclidean_distance(city, u) for u in unvisited if u != city]))
        if max_dist_for_city < min_max_dist:
            min_max_dist = max_dist_for_city
            next_city = city
    return next_city

# Generate the tour starting from the depot city (0)
def generate_tour():
    tour = [0]
    total_cost = 0
    max_leg_cost = 0
    unvisited = set(range(1, num_cities))
    current_city = 0

    while unvisited:
        next_city = find_min_max_edge_city(current_city, unvisited)
        tour.append(next_city)
        leg_cost = euclidean_distance(current_city, next_city)
        total_cost += leg_cost
        max_leg_cost = max(max_leg_cost, leg_cost)
        unvisited.remove(next_city)
        current_city = next_city

    # Close the tour returning to the depot city
    final_leg_cost = euclidean_distance(current_city, 0)
    total_cost += final_leg_cost
    max_leg_cost = max(max_leg_cost, final_leg_cost)
    tour.append(0)

    return tour, total_cost, max_leg_cost

tour, total_cost, max_leg_cost = generate_tour()

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_cost)