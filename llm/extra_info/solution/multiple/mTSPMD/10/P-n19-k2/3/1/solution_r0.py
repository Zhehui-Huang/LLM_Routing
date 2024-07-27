import math
import itertools

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Assign cities to depots (simple allocation)
city_assignment = {}
city_assignment[0] = [0]  # Depot for robot 0
city_assignment[1] = [1]  # Depot for robot 1

non_depot_cities = [city for city in cities if city not in [0, 1]]
half_cities = len(non_depot_cities) // 2
city_assignment[0].extend(non_depot_cities[:half_cities])
city_assignment[1].extend(non_depot_cities[half_cities:])

# Simple greedy TSP solver
def tsp_tour(depots, allocated_cities):
    path = [depots]
    unvisited = set(allocated_cities)
    current = depots

    while unvisited:
        next_city = min(unvisited, key=lambda x: distance(current, x))
        path.append(next_city)
        unvisited.remove(next_city)
        current = next_city
        
    path.append(depots) # Add return to depot
    return path

# Calculate tour and cost
def calculate_tour_and_cost(depots, cities):
    tour = tsp_tour(depots, cities)
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return tour, tour_cost

# Compute tours and costs for each robot
tour_data = {}
overall_cost = 0

for robot_id, depots in enumerate([0, 1]):
    tour, cost = calculate_tour_and_cost(depots, city_assignment[robot_id][1:])
    tour_data[robot_id] = {"tour": tour, "cost": cost}
    overall_cost += cost

# Output the results
for robot_id, data in tour_data.items():
    print(f"Robot {robot_id} Tour: {data['tour']}")
    print(f"Robot {robot_id} Total Travel Cost: {data['cost']}")

print(f"Overall Total Travel Cost: {overall_cost}")