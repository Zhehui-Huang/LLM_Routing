import numpy as
from scipy.spatial import distance_matrix

# City coordinates as a list of tuples for easier distance matrix computation
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 61), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

cities = list(city_coordinates.values())
distance_matrix = distance.cdist(cities, cities, metric='euclidean')

def nearest_neighbor_tours(start_city, num_robots, distance_matrix):
    num_cities = len(distance_matrix)
    visited = np.zeros(num_cities, dtype=bool)
    visited[start_city] = True
    tours = [[start_city] for _ in range(num_robots)]
    robot_positions = [start_city] * num_robots
    remaining_cities = set(range(num_cities)) - {start_city}

    while remaining_cities:
        for robot_id in range(num_robots):
            if remaining_cities:
                nearest_city = min(
                    remaining_cities,
                    key=lambda city: distance_matrix[robot_positions[robot_id]][city]
                )
                tours[robot_id].append(nearest_city)
                robot_positions[robot_id] = nearest_city
                remaining_cities.remove(nearest_city)

    return tours

tours = nearest_neighbor_tours(0, 8, distance_matrix)

def calculate_cost(tours, distance_matrix):
    total_travel_cost = 0
    costs = []

    for tour in tours:
        tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        costs.append(tour_cost)
        total_travel_in_cost += tour_cost

    return costs, total_travel_cost

costs, total_travel_cost = calculate_cost(tours, distance_matrix)

# Print the solution
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {total_travel_cost}")