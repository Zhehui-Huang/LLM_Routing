import math
import random

# Define the cities coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Euclidean distance between two cities
def distance(city1_id, city2_id):
    x1, y1 = cities[city1_id]
    x2, y2 = cities[city2_id]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize tours by distributing cities evenly among robots
def initialize_tours(num_robots):
    city_ids = list(cities.keys())[1:]  # exclude the depot city
    random.shuffle(city_ids)
    tours = [[] for _ in range(num_robots)]
    for index, city_id in enumerate(city_ids):
        tours[index % num_robots].append(city_id)
    return tours

# Calculate the cost of a specific tour
def calculate_tour_cost(tour):
    tour_distance = 0
    tour_distance += distance(0, tour[0])  # from depot to first city
    for i in range(len(tour) - 1):
        tour_distance += distance(tour[i], tour[i+1])
    tour_distance += distance(tour[-1], 0)  # return to depot
    return tour_distance

# Attempt to improve the tours by minimizing the maximum tour length
def optimize_tours(tours):
    def try_swap(tours, i, j, k, l):
        tours[i][j], tours[k][l] = tours[k][l], tours[i][j]  # swap
        new_max_cost = max(calculate_tour_cost(tour) for tour in tours_with_depots)
        if new_max_cost < current_max_cost:
            return new_max_cost
        else:
            tours[i][j], tours[k][l] = tours[k][l], tours[i][j]  # swap back
            return None

    improvement = True
    while improvement:
        improvement = False
        tours_with_depots = [[0] + tour + [0] for tour in tours]
        current_max_cost = max(calculate_tour_cost(tour) for tour in tours_with_depots)
        for i in range(len(tours)):
            for j in range(len(tours[i])):
                for k in range(i, len(tours)):
                    start = 0 if i == k else j + 1
                    for l in range(start, len(tours[k])):
                        result = try_swap(tours, i, j, k, l)
                        if result is not None:
                            current_max_cost = result
                            improvement = True

# Main function to solve mTSP
def solve_mTSP(num_robots):
    tours = initialize_tours(num_robots)
    optimize_tours(tours)
    max_cost = 0
    for index, tour in enumerate(tours):
        tour_with_depot = [0] + tour + [0]
        tour_cost = calculate_tour_cost(tour)
        max_cost = max(max_cost, tour_cost)
        print(f"Robot {index} Tour: {tour_with_depot}")
        print(f"Robot {index} Total Travel Cost: {tour_cost}")
    print(f"Maximum Travel Cost: {max_cost}")

# Assume number of robots is given
num_robots = 8
solve_mTSP(num_robots)