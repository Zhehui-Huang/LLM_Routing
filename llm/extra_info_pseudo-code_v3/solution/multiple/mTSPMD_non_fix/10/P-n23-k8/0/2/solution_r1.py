import math

# Coordinates setup for each city
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Helper function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Nearest Neighbor to generate an initial solution for a single tour starting from a given depot
def nearest_neighbor_tour(start_city, available_cities):
    tour = [start_city]
    current_city = start_city
    
    while available_cities:
        next_city = min(available_cities, key=lambda x: euclidean_distance(current_city, x))
        tour.append(next_city)
        available_cities.remove(next_city)
        current_city = next_city

    return tour

# Split the cities among the available robots
def distribute_cities_to_robots(num_robots, cities):
    city_list = list(cities.keys())
    city_list.remove(0)  # Remove the depot city from the list to be assigned
    random.shuffle(city_list)  # Randomize city order
    return [city_list[i::num_robots] for i in range(num_robots)]

# Calculate tour costs
def calculate_tour_cost(tour):
    cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return cost

# Create initial solutions
city_groups = distribute_cities_to_robots(num_robots=num_robots, cities=cities)
tours = [nearest_neighbor_tour(0, set(group)) for group in city_groups]  # All start at depot 0

# Output tours and their costs
overall_cost = 0
for idx, tour in enumerate(tours):
    cost = calculate_tour_cost(tour + [0])  # Include returning to the starting depot
    overall_cost += cost
    print(f"Robot {idx} Tour: [0, {' -> '.join(map(str, tour))}, 0]")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")