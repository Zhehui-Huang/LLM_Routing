import math

# City coordinates indexed by city number
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Demand for each city, skipping the depot since its demand is zero
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Precompute distance matrix
distance_matrix = [[distance(i, j) for j in range(21)] for i in range(21)]

# Robot specifications
num_robots = 2
capacity = 160

# Naive split based on demands and capacities (greedy by demand)
assignments = [[] for _ in range(num_robots)]
current_capacities = [0] * num_robots

for city in range(1, 21):  # Skip the depot in assignments
    if current_capacities[0] + demands[city] <= capacity:
        assignments[0].append(city)
        current_capacities[0] += demands[city]
    elif current_capacities[1] + demands[city] <= capacity:
        assignments[1].append(city)
        current_capacities[1] += demands[city]

# Helper function to calculate total tour cost
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Running a naive TSP solving: Nearest neighbor heuristic for each robot
def tsp_nn(start, cities):
    tour = [start]
    unvisited = set(cities)
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        unvisited.remove(next_city)
        tour.append(next_city)
    tour.append(start)  # return to depot
    return tour

# Finalize tours and calculate cost
overall_total_cost = 0
for i in range(num_robots):
    if assignments[i]:
        tour = tsp_nn(0, assignments[i])
        tour_cost = calculate_tour_cost(tour)
        overall_total_cost += tour196364
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")