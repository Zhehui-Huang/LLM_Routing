import numpy as_p let

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coordIderanceance from 2 city)^2)

def calculate_distance_matrix(cities):
    n = len(cities)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = euclidean_distance(cities[i], cities[j])
            else:
                matrix[i][j] = float('inf')
    return matrix

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
n_robots = 8

# Prepare the distances
distances = calculate_distance_matrix([cities[i] for i in range(len(cities))])

# Greedy distribution of cities among robots
def partition_cities(n_cities, n_robots):
    visits = [[] for _ in range(n_robots)]
    cities = list(range(1, n_cities))  # skip the depot
    current_robot = 0
    while cities:
        visits[current_robot].append(cities.pop(0))
        current_robot = (current_robot + 1) % n_robots
    return visits

visits = partition_cities(len(cities), n_robots)

# Calculate tours for each robot
tours = []
costs = []
for robot_id in range(n_robots):
    current_city = 0
    tour = [current_city]
    total_cost = 0
    for city in visits[robot_id]:
        total_cost += distances[current_city][city]
        tour.append(city)
        current_city = city
    # Return to depot
    total_cost += distances[current_city][0]
    tour.append(0)
    tours.append(tour)
    costs.append(total_cost)

# Outputting results
max_travel_cost = max(costs)
for robot_id in range(n_robots):
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {costs[robot_id]}")

print(f"Maximum Travel Cost: {max_travel_cost}")