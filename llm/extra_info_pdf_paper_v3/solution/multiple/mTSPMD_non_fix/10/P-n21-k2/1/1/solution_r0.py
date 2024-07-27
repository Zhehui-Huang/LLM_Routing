import math
import random

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def total_cost_of_tour(tour, coordinates):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def simulated_annealing(coords, depot_starts, num_robots):
    current_sol = [[] for _ in range(num_robots)]
    cities = list(range(len(coords)))
    random.shuffle(cities)

    # Distribute cities to robots initially
    for i, city in enumerate(cities):
        current_sol[i % num_robots].append(city)

    def swap_random(tour):
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]

    def simulated_annealing_internal(tour):
        temp = initial_temp = 10000
        final_temp = 1
        alpha = 0.995
        current_tour = tour[:]
        current_cost = total_cost_of_tour(current_tour, coords)
        while temp > final_temp:
            new_tour = current_tour[:]
            swap_random(new_tour)
            new_cost = total_cost_of_tour(new_tour, coords)
            cost_diff = new_cost - current_cost
            if cost_diff < 0 or random.random() < math.exp(-cost_diff / temp):
                current_tour = new_tour
                current_cost = new_cost
            temp *= alpha
        return current_tour, current_cost

    final_solution = []
    total_travel_cost = 0
    
    for index, robot_tour in enumerate(current_sol):
        start = robot_tour.pop(0)
        robot_tour.insert(0, depot_starts[index % len(depot_starts)])
        robot_tour.append(start)
        best_tour, best_cost = simulated_annealing_internal(robot_tour)
        final_solution.append(best_tour)
        total_travel_cost += best_cost

    return final_solution, total_travel_cost

# Coordinates of all cities, indexed accordingly
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

depots = [0, 1]

# Run simulation
final_tours, overall_cost = simulated_annealing(coordinates, depots, 2)
print("Overall Total Travel Cost:", overall_cost)
for i, tour in enumerate(final_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {total_cost_of_tour(tour, coordinates)}")