import math
import random

# Environment information
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
num_robots = 8
depots = list(range(num_robots))  # Depots range from 0 to 7, assuming each robot starts from depot 0

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize robots tours starting from depot
tours = {robot_id: [0] for robot_id in range(num_robots)}  # All robots start at depot city 0

# Step 1: Assign a unique city to each tour for initial points
remaining_cities = set(cities.keys()) - {0}

for robot_id in tours:
    nearest_city = min(remaining_cities, key=lambda city: distance(tours[robot_id][-1], city))
    tours[robot_id].append(nearest_city)
    remaining_cities.remove(nearest_city)

# Step 2: As long as there are cities to visit, extend each robots' tour with the nearest city
while remaining_cities:
    for robot_id, tour in tours.items():
        if not remaining_cities:
            break
        nearest_city = min(remaining_cities, key=lambda city: distance(tour[-1], city))
        tour.append(nearest_city)
        remaining_cities.remove(nearest_city)

# Step 3: Calculate the travel cost for each robot tour
total_costs = {}
overall_total_cost = 0

for robot_id, tour in tours.items():
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance(tour[i - 1], tour[i])
    tours[robot_id].append(0) # Assuming they don't need to return to any depot, just terminate at the last city
    total_cost += distance(tour[-2], 0)  # However, to adhere to guidelines, we add the return to depot 0
    total_costs[robot_comp_id] = total_cost
    overall_total_cost += total_cost

    print(f"Robot {robot_comp_id} Tour: {tours[robot_comp_id]}")
    print(f"Robot {robot_comp_id} Total Travel Cost: {total_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")