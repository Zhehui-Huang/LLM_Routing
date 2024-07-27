import math

# City coordinates list
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Define robots and their depots
robot_depots = {0: 0, 1: 1, 2: 2, 3: 3}

# Euclidean distance calculation
def euclidean_distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Assign cities to robots based on a naive rounding-robin method purely as an example
city_assignment = {i: [] for i in range(4)}
for i, coord in enumerate(city_coords):
    if i in robot_depots.values():
        continue
    city_assignment[i % 4].append(i)
for robot, cities in city_assignment.items():
    city_assignment[robot] = [robot_depots[robot]] + cities + [robot_depots[robot]]

# Calculate the tours using a greedy algorithm based on minimum additional cost to include a city
def compute_tour(cities):
    start_city = cities.pop(0)
    tour = [start_city]
    while cities:
        next_city = min(cities, key=lambda x: euclidean_distance(tour[-1], x))
        tour.append(next_city)
        cities.remove(next_city)
    tour.append(start_city)
    return tour

# Calculating tours and costs
total_cost = 0
for robot in range(4):
    tour = compute_tour(city_assignment[robot].copy())
    cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {round(cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")