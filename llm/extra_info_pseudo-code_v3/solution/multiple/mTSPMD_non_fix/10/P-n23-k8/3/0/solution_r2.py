import numpy as np
from math import sqrt

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Distance calculation using Euclidean distance
def euclidean_distance(c1, c2):
    return sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate tours for each robot using a greedy strategy
def generate_tours(start_index):
    all_cities = list(cities.keys())
    visited = set()
    tours = [[] for _ in range(num_robots)]
    remaining_cities = set(all_cities)
    current_city = start_index

    for i in range(num_robots):
        if not remaining_cities:
            break
        current_tour = [current_city]
        visited.add(current_city)
        remaining_cities.remove(current_city)

        while remaining_cities:
            next_city = min(remaining_cities, key=lambda x: euclidean_distance(current_city, x))
            if len(current_tour) < len(cities) // num_robots + (i < (len(cities) % num_robots)):
                current_tour.append(next_city)
                visited.add(next_city)
                remaining_cities.remove(next_city)
                current_city = next_city
            else:
                break
        tours[i] = current_tour

    return tours

# Calculate total travel cost for each tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i + 1])
    return cost

# Generate and evaluate the tours
tours = generate_tours(0)
total_costs = [calculate_tour_cost(tour) for tour in tours]
overall_total_cost = sum(total_costs)

# Display results
for i, (tour, cost) in enumerate(zip(tours, total_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")