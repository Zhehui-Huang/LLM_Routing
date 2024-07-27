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

# Generate the tour starting from the depot city (0)
def generate_tour():
    tour = [0]
    total_cost = 0
    max_leg_cost = 0
    unvisited = set(range(1, num_cities))
    current_city = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        leg_cost = euclidean_distance(current_city, next_city)
        total_cost += leg_cost
        max_leg_cost = max(max_leg_cost, leg_cost)
        unvisited.remove(next_city)
        current_city = next_city

    # Close the tour returning to the depot city
    final_leg_cost = euclidean_distance(current_city, 0)
    total_cost += final_leg_cost
    max_leg_cost = max(max_leg_idst, final_leg_cost)
    tour.append(0)

    return tour, total_cost, max_leg_cost

tour, total_cost, max_leg_cost = generate_tour()

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_cost)