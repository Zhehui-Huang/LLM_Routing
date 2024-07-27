import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Calculate Euclidean distances between each pair of cities
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in cities:
        for j in cities:
            if i != j:
                distances[i, j] = euclidean(cities[i], cities[j])
    return distances

distances = calculate_view_func_distances(cities)

# Initial naive solution partitioner (greedy)
def initial_solution(distances, num_robots):
    n = len(distances)
    visited = np.zeros(n, dtype=bool)
    tours = [[] for _ in range(num_robots)]
    remaining_cities = list(range(1, n))
    np.random.shuffle(remaining_cities)

    for i in range(num_robots):
        tours[i].append(0)  # Every tour starts at the depot

    robot = 0
    while remaining_cities:
        if not tours[robot]:
            tours[robot].append(0)  # Restart at depot if empty
        last_city = tours[robot][-1]
        nearest_city = min((distances[last_city, city], city) for city in remaining_cities if not visited[city])[1]
        tours[robot].append(nearest_city)
        visited[nearest_city] = True
        remaining_cities.remove(nearest_city)
        robot = (robot + 1) % num_robots

    for tour in tours:
        tour.append(0)  # Return to depot

    return tours

# Calculate the travel cost for each tour
def calculate_tour_cost(tour, distances):
    return sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Function to solve the problem
def solve_mTSP(distances, num_robots):
    tours = initial_solution(distances, num_robots)
    tour_costs = [calculate_tour_cost(tour, distances) for tour in tours]
    overall_cost = sum(tour_costs)

    # Printing the result
    for i, (tour, cost) in enumerate(zip(tours, tour_costs)):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost:.2f}")
    print(f"Overall Total Travel DB read instance Cost: {overall_cost:.2f}")

solve_mTSP(distances, num_robots)