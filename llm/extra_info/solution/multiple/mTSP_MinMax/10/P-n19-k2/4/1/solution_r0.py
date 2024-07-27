import numpy as np

# City coordinates (city index corresponds to coordinates index)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

n_cities = len(coordinates)
distance_matrix = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Solve the TSP using a simple heuristic: Nearest Neighbor for two robots
def solve_tsp_two_robots(distance_matrix, start_city=0, num_robots=2):
    remaining_cities = set(range(1, n_cities))  # Exclude depot initially
    tours = [[] for _ in range(num_robots)]
    tour_costs = [0] * num_robots

    # Start each robot tour at the depot
    for i in range(num_robots):
        tours[i].append(start_city)

    current_cities = [start_city] * num_robots

    # Assign cities to each robot
    while remaining_cities:
        for i in range(num_robots):
            if not remaining_cities:
                break
            # Find the nearest unvisited city
            nearest_city = min(remaining_cities, key=lambda x: distance_matrix[current_cities[i]][x])
            tours[i].append(nearest_city)
            tour_costs[i] += distance_matrix[current_cities[i]][nearest_city]
            current_cities[i] = nearest_city
            remaining_cities.remove(nearest_city)
    
    # Return all robots to the start city
    for i in range(num_robots):
        tours[i].append(start_city)
        tour_costs[i] += distance_matrix[current_cities[i]][start_city]
    
    return tours, tour_costs

tours, tour_costs = solve_tsp_two_robots(distance_matrix)
max_cost = max(tour_costs)

# Output the results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")