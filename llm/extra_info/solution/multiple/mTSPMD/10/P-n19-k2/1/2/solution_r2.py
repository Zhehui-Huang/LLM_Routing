import math

# Cities and their Coordinates: Index maps to coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}
depots = {0: 0, 1: 1}

# Distance calculation function
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Partition cities between robots based on closest depot
robot_assignments = {0: [0], 1: [1]}
for city in range(2, len(cities)):
    closest_depot = min(depots, key=lambda depot: euclidean_distance(city, depot))
    robot_assignments[closest_depot].append(city)

# Generate tours for each robot using a simple Nearest Neighbor heuristic
def nearest_neighbor_tour(start, assigned_cities):
    tour = [start]
    unvisited = set(assigned_cities)
    unvisited.remove(start)

    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda city: euclidean_distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)  # complete the loop by returning to the depot
    return tour

# Calculate tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Determine tours and costs
tours = {}
total_costs = {}
overall_total_cost = 0

for robot_id in robot_assignments:
    tour = nearest_neighbor_tour(depots[robot_id], robot_assignments[robot_id])
    cost = calculate_tour_cost(tour)
    tours[robot_id] = tour
    total_costs[robot_id] = cost
    overall_total_cost += cost

# Display the results clearly
for robot_id in sorted(tours):
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {total_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")