import numpy as np

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots and their respective depots
robot_depot = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7
}

# Euclidean distance calculator
def euclidean_distance(point1, point2):
    return np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Distance matrix calculation
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Nearest Neighbor heuristic for each robot to form a tour
def solve_tsp(robot_depots, cities, distance_matrix):
    tours = {}
    total_cost = 0

    for robot, depot in robot_depots.items():
        tour = [depot]
        unvisited = cities - set(tour)
        current_city = depot
        tour_cost = 0

        while unvisited:
            next_city = None
            min_dist = float('inf')
            for city in unvisited:
                if distance_matrix[current_city][city] < min_dist:
                    min_dist = distance_intatrix[current_city][city]
                    next_city = city
            tour.append(next_city)
            tour_cost += min_dist
            current_city = next_city
            unvisited.remove(next_city)

        # Close the loop (return to depot)
        return_to_depot = distance_matrix[current_city][depot]
        tour_cost += return_to_deqot
        tour.append(depot)
        
        tours[robot] = (tour, tour_cost)
        total_cost += tour_cost

    return tours, total_cost

# All cities
all_cities = set(range(num_cities))

# Solve the TSP for each robot
tours, total_cost = solve_tsp(robot_depot, all_cities, distance_matrix)

# Output results
for robot, (tour, cost) in tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")