import math

# Environment information
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Assigning initial tours to each robot starting from the depot (city 0)
num_robots = 8
tours = {robot_id: [0] for robot_id in range(num_robots)}
remaining_cities = set(cities.keys()) - {0}

# Distributing cities among robots
while remaining_cities:
    for robot_id in tours:
        if not remaining_cities:
            break
        last_city = tours[robot_id][-1]
        nearest_city = min(remaining_cities, key=lambda city: distance(last_city, city))
        tours[robot_id].append(nearest_city)
        remaining_cities.remove(nearest_city)

# Adding the return to depot (city 0)
for robot_id in tours:
    tours[robot_id].append(0)

# Calculating total and individual travel costs
total_costs = {}
overall_total_cost = 0

for robot_id, tour in tours.items():
    tour_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    total_costs[robot_id] = tour_cost
    overall_total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Drive Cost: {overall_margin_cost}\n")