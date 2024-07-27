import math
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 65), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of robots
num_robots = 2

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def initialize_tours():
    total_cities = list(cities.keys())[1:]  # Exclude the depot city index (0)
    random.shuffle(total_cities)
    avg_cities_per_robot = len(total_cities) // num_robots
    tours = []
    for i in range(num_robots):
        if i == num_robots - 1:
            tours.append([0] + total_cities[i * avg_cities_per_robot:] + [0])
        else:
            tours.append([0] + total_cities[i * avg_cities_per_robot:(i + 1) * avg_cities_per_robot] + [0])
    return tours

def optimize_tours(tours):
    # Local optimization function to swap two cities and check if the tour improves
    def local_improve(tour):
        best_cost = calculate_tour_cost(tour)
        improved = True
        while improved:
            improved = False
            for i in range(1, len(tour) - 2):
                for j in range(i + 1, len(tour) - 1):
                    new_tour = tour[:i] + [tour[j]] + tour[i + 1:j] + [tour[i]] + tour[j + 1:]
                    new_cost = calculate_tour_cost(new_tour)
                    if new_cost < best_cost:
                        tour = new_tour
                        best_cost = new_cost
                        improved = True
                        break
                if improved:
                    break
        return tour

    for i in range(len(tours)):
        tours[i] = local_improve(tours[i])
    return tours

def solve_mTSP():
    tours = initialize_tours()
    tours = optimize_tours(tours)
    costs = [calculate_tour_cost(tour) for tour in tours]
    max_cost = max(costs)

    # Output tour details and their costs
    for i, tour in enumerate(tours):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {costs[i]}")
    print(f"Maximum Travel Cost: {max_cost}")

solve_mTSP()