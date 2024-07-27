import math

# Step 1: Define the cities and their coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Step 2: Calculate Euclidean distances between all pairs of cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

n = len(cities)
distance_matrix = [[calculate_distance(i, j) for j in range(n)] for i in range(n)]

# Step 3: Simulate a greedy TSP solver
def greedy_tsp(start_city, cities, distance_matrix):
    tour = [start_city]
    to_visit = set(cities.keys()) - {start_city}

    while to_visit:
        nearest = min(to_visit, key=lambda x: distance_matrix[tour[-1]][x])
        tour.append(nearest)
        to_visit.remove(nearest)

    tour.append(start_city)  # complete the circuit
    return tour

tsp_tour = greedy_tsp(0, cities, distance_matrix)

# Step 4: Divide tasks equally among robots
num_robots = 4
segments = len(tsp_tour) // num_robots
robot_tours = [[0] for _ in range(num_robots)]

for index, city in enumerate(tsp_tour[1:-1], 1):
    robot_id = (index - 1) // segments
    if robot_id < num_robots:
        robot_tours[robot_id].append(city)
    else:
        robot_tours[-1].append(city)
        
for rt in robot_tours:
    rt.append(0)  # ensure each robot returns to the depot

# Step 5: Calculate the cost of each route and the maximum travel cost
def get_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

costs = [get_tour_cost(tour, distance_matrix) for tour in robot_tours]
max_cost = max(cost]s]])

# Output the results
for i, tour in enumerate(robot_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]:.2f}")

print(f"Maximum Travel Cap Cost: {max_cost:.2f}")