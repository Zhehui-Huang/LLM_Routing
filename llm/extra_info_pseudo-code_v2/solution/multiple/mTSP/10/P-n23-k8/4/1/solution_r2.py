import math

# Environment information
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
num_robots = 8

# Euclidean distance calculation
def calc_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Calculate all distances between cities
distances = [[calc_distance(i, j) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Assign cities to robots heuristically to balance the workload
cities_per_robot = len(coordinates[1:]) // num_robots
assignments = [list(range(1 + i * cities_per_robot, 1 + (i + 1) * cities_per_robot)) for i in range(num_robots)]
for i in range(len(coordinates[1:]) % num_robots):
    assignments[i].append(1 + num_robots * cities_per_robot + i)

# Nearest neighbor heuristic to create initial tours
def nearest_neighbor_tour(starting_city, cities):
    unvisited = cities[:]
    tour = [starting_city]
    current_city = starting_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        current_city = next_city
        unutilized = unvisited.remove(next_city)
    tour.append(starting_city)  # return to depot
    return tour

def tour_cost(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Initialize tours
tours = [nearest_neighbor_tour(0, assignment) for assignment in assignments]

# Perform 2-opt to improve each tour
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # These are consecutive edges
                if distances[tour[i]][tour[i-1]] + distances[tour[j]][tour[(j+1)%len(tour)]] > \
                   distances[tour[i]][tour[j]] + distances[tour[i-1]][tour[(j+1)%len(tour)]]:
                    tour[i:j] = tour[i:j][::-1]  # Reverse part of the tour
                    improved = True
    return tour

# Improve tours
tours = [two_opt(tour) for tour in tours]

# Calculate total costs
costs = [tour_cost(tour) for tour in tours]
overall_cost = sum(costs)

# Output results
for robot_id, tour in enumerate(tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {costs[robot_id]}")
print(f"Overall Total Travel Cost: {overall_cost}")