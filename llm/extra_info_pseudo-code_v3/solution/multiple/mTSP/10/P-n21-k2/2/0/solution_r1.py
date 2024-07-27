import math

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
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

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def compute_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Splitting the cities between two robots
cities_per_robot = {0: [0], 1: [0]}

# Distributing cities to robots
for i, city_id in enumerate(range(1, 21), 1):
    cities_per_robot[i % 2].append(city_id)

# Make sure both tours start and end at the depot
for robot_id in cities_per_robot:
    cities_per_robot[robot_id].append(0)

tour_costs = {}
total_travel_cost = 0

for robot_id in cities_per_robot:
    tour = cities_per_robot[robot_id]
    cost = compute_tour_cost(tour)
    tour_costs[robot_id] = {'tour': tour, 'cost': cost}
    total_travel_cost += cost

# Output Tours and Costs
for robot_id, data in tour_costs.items():
    print(f"Robot {robot_id} Tour: {data['tour']}")
    print(f"Robot {robot_id} Total Travel Cost: {data['cost']}")

print(f"Overall Total Travel Cost: {total_travel_cost}")