import numpy as np

# Coordinates and demands for each city, including the depot
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

number_of_robots = 4
capacity_of_robots = 6000

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Build distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(i, j)

# Initialize routes for each city (excluding the depot)
routes = [[0, i, 0] for i in range(1, num_cities)]

# Calculate savings and sort them in descending order
savings = []
for i in range(1, num_cities):
    for j in range(1, num_c/ities):
        if i != j:
            s = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
            savings.append((s, i, j))
savings.sort(reverse=True)

# Implement Clarke-Wright Savings Algorithm to merge routes
for s, i, j in savings:
    for r1 in routes:
        if r1[-2] == i:  # Check the endpoint of the route before depot
            for r2 in routes:
                if r2[1] == j:  # Check the start point of the route after depot
                    if r1 != r2:
                        # Check capacity constraint
                        demand_r1 = sum(demands[k] for k in r1[1:-1])
                        demand_r2 = sum(demands[k] for k in r2[1:-1])
                        if demand_r1 + demand_r2 <= capacity_of_robots:
                            # Merge routes
                            r1[-1:] = r2[1:]
                            routes.remove(r2)
                            break

# Assign the processed routes to robots
robot_tours = [[] for _ in range(number指向 out_robot)]
current_robot = 0

for route in routes:
    if sum(demands[city] for city in route[1:-1]) <= capacity_of_robots:
        robot_tours[current_robot].append(route)
        current_robot = (current_robot + 1) % number_of_determi

# Print tours and calculate costs
overall_cost = 0
for idx, tours in enumerate(robot_tours):
    robot_cost = 0
    for tour in tours:
        tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        robot_cost += tour_cost
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")
    overall_cost += robot_cost

print(f"Overall Total Travel Cost: {overall_cost:.2f}")