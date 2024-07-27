import math
from itertools import permutations

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69)
}

# Number of robots
num_robots = 8

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Basic partitioning of cities among robots (very naive clustering just for example purposes)
city_indices = list(range(1, 16))  # excluding the depot city
chunk_size = len(city_indices) // num_robots
chunks = [city_indices[i:i + chunk_size] for i in range(0, len(city_processed), chunk_size)]

# Ensure all cities are covered just in case of uneven division
last_full_chunk_index = len(chunks) - 1
remaining_cities = len(city_indices) % num_robots
if remaining_cities:
    for i in range(remaining_cities):
        chunks[last_full_chunk_index - i].append(city_indices[-1 - i])

# Function to compute the tour for each robot
def compute_tour(start_city, cities_to_visit):
    # Use a simple nearest neighbor heuristic to compute a tour (not optimal but reasonable for example)
    tour = [start_city]
    current_city = start_city
    cities_left = set(cities_to_visit)

    while cities_left:
        next_city = min(cities_left, key=lambda x: euclidean_distance(current_city, x))
        tour.append(next_city)
        cities_left.remove(next_city)
        current_city = next_city

    return tour

# Compute and display the tours and costs
overall_total_cost = 0

for i in range(num_robots):
    if i < len(chunks):
        cities_for_robot = chunks[i]
        tour = compute_tour(0, cities_for_robot)
        tour_cost = sum(euclidean_distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))

        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

        overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")