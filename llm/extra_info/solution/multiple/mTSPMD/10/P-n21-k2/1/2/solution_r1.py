import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to solve TSP using nearest neighbor plus manual improvements
def solve_tsp(start, tour_cities):
    tour = [start]
    unvisited = set(tour_cities) - {start}
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda city: euclidean_distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)  # return to depot
    return tour

# Split city ids into two groups (excluding depots), one for each robot
group_1 = [2, 3, 4, 6, 7, 8, 10, 11, 12, 15, 16]
group_2 = [5, 9, 13, 14, 17, 18, 19, 20]

# Solve for both robots
robot_0_tour = solve_tsp(0, group_1 + [0])
robot_1_tour = solve_tsp(1, group_2 + [1])

# Calculate travel costs
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i + 1])
    return cost

robot_0_cost = calculate_tour_cost(robot_0_tour)
robot_1_cost = calculate_tour_cost(robot_1_tour)
total_cost = robot_0_cost + robot_1_cost

# Output the results
print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost:.2f}")
print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost:.2f}")
print(f"Overall Total Travel Cost: {total_cost:.2f}")