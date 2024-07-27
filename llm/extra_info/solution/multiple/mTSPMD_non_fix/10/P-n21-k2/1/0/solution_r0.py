import math

# City coordinates with their indices
cities = {
    0: (30, 40),  # Depot 0
    1: (37, 52),  # Depot 1
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Construct a greedy solution based on nearest neighbor heuristic
def nearest_neighbor_tour(start, cities_to_visit):
    tour = [start]
    while cities_to_visit:
        last = tour[-1]
        next_city = min(cities_to_visit, key=lambda city: distance(last, city))
        cities_to_visit.remove(next_city)
        tour.append(next_city)
    return tour

# Splitting the cities approximately evenly starting from each depot
cities_from_0 = [2, 5, 6, 7, 9, 14, 17, 20]
cities_from_1 = [3, 4, 8, 10, 11, 12, 15, 16, 18, 19]

# Compute tours for each robot
tour_robot_0 = nearest_neighbor_tour(0, set(cities_from_0))
tour_robot_1 = nearest_neighbor_tour(1, set(cities_from_1))

# Function to calculate total travel cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Costs
cost_robot_0 = tour_cost(tour_robot_0)
cost_robot_1 = tour_cost(tour_robot_1)
overall_cost = cost_robot_0 + cost_robot_1

# Output the results
print(f"Robot 0 Tour: {tour_robot_0}")
print(f"Robot 0 Total Travel Cost: {cost_robot_0:.2f}")
print(f"Robot 1 Tour: {tour_robot_1}")
print(f"Robot 1 Total Travel Cost: {cost_robot_1:.2f}")
print(f"Overall Total Travel Cost: {overall_cost:.2f}")