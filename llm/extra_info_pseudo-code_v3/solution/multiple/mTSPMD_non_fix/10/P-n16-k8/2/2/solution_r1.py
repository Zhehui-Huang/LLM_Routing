import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialization with city coordinates and robot information
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Initialize tours for each robot, starting from depot 0
num_robots = 8
tours = {robot: [0] for robot in range(num_robots)}

# Remaining unvisited cities
unvisited_cities = set(cities.keys()) - {0}

# Nearest Neighbor initial solution
while unvisited_cities:
    for robot in tours:
        if not unvisited_cities:
            break
        current_city = tours[robot][-1]
        nearest_city = min(unvisited_cities, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        tours[robot].append(nearest_city)
        unvisited_cities.remove(nearest_city)

# Ensure that each robot's tour ends at a depot (for qualitative improvement, not required by the problem as per given statement)
# Here we assume the robot ends at nearest depot. As per problem statement, it is optional.
for robot in tours:
    tours[robot].append(0)

# Calculate total travel cost for each tour and the combined cost
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

overall_total_cost = 0
for robot, tour in tours.items():
    tour_cost = calculate_total_cost(tour)
    overall_total_cost += tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_geom_cost}")