import math
import random

# City Coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

def simulated_annealing(tour, initial_temp, cooling_rate, num_iterations):
    def total_tour_cost(tour):
        return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

    current_temp = initial_temp
    current_tour = tour[:]
    current_cost = total_tour_cost(current_tour)
    best_tour = current_tour[:]
    best_cost = current_cost

    for _ in range(num_iterations):
        next_tour = current_tour[:]
        # Swap two random elements in the tour (except the start, which is the depot)
        l, r = random.sample(range(1, len(tour) - 1), 2)
        next_tour[l], next_tour[r] = next_tour[r], next_tour[l]
        next_cost = total_tour_cost(next_tour)

        if next_cost < current_cost or random.random() < math.exp((current_cost - next_cost) / current_temp):
            current_tour, current_cost = next_tour, next_cost
            if current_cost < best_cost:
                best_tour, best_cost = current_tour[:], current_cost

        current_temp *= cooling_rate

    return best_tour, best_cost

# Assign cities to robots: Each robot starts at depot 0 (index 0)
robot_assignments = {
 0: [1, 2, 3, 4, 5],
 1: [6, 7, 8, 9, 10],
 2: [11, 12, 13, 14, 15],
 3: [16, 17, 18, 19, 20, 21]
}

initial_temp = 100
cooling_rate = 0.995
num_iterations = 2000

tours = []
costs = []
overall_cost = 0

for robot_id, assigned_cities in robot_assignments.items():
    tour, cost = simulated_annealing([0] + assigned_cities, initial_temp, cooling_rate, num_iterations)
    tours.append(tour)
    costs.append(cost)
    overall_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")