import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 
           600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 
           2500, 1800, 700]

# Calculate distances between all cities
num_cities = len(coordinates)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean_distance(*coordinates[i], *coordinates[j])

# Robot details
num_robots = 4
robot_capacity = 6000

# Clustering cities based on demand and robot capacity
clusters = []
current_cluster = []
current_capacity = 0

for i in range(1, num_cities):  # start from 1 to skip the depot
    if current_capacity + demands[i] <= robot_capacity:
        current_cluster.append(i)
        current_capacity += demands[i]
    else:
        clusters.append(current_cluster)
        current_cluster = [i]
        current_capacity = demands[i]

if current_cluster:
    clusters.append(current_cluster)

# Creating tours for robots (ensure no more robots than clusters)
robot_tours = []
total_travel_cost = 0

def calculate_tour_cost(tour):
    cost = 0
    for k in range(len(tour) - 1):
        cost += distances[tour[k]][tour[k + 1]]
    return cost

for cluster in clusters:
    tour = [0] + cluster + [0]  # start and end at depot
    cost = calculate_tour_cost(tour)
    robot_tours.append((tour, cost))
    total_travel_cost += cost

# Outputting results
for idx, (tour, cost) in enumerate(robot_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_cost:.2f}")