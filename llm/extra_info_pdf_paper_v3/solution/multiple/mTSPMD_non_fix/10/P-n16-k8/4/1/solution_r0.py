import math
import random

# Defining the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41), 
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots
num_robots = 8

# Distance calculation function
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize the distance matrix
dist_matrix = {}
for i in cities:
    for j in cities:
        dist_matrix[(i, j)] = distance(i, j) if i != j else 0

# Initial solution generation randomly as a starting point for SA
def generate_initial_solution():
    cities_list = list(cities.keys())[1:]  # excluding the depot to distribute among robots
    random.shuffle(cities_list)
    # Assign equal number of cities to each robot
    size = len(cities_list) // num_robots
    solutions = [cities_list[i*size:(i+1)*size] for i in range(num_robots)]
    for i, tour in enumerate(solutions):
        if i == 0:
            tour.insert(0, 0)  # appending the depot for the first robot
            tour.append(0)  # assuming return to depot for simplicity in initial guess
    return solutions

# Cost of the tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += dist_matrix[tour[i], tour[i+1]]
    return cost

# Simulated Annealing implementation for a single tour
def simulated_annealing(tour):
    temp = 10000
    cooling_rate = 0.995
    min_temp = 0.01

    current_tour = tour[:]
    current_cost = calculate_tour_cost(current_tour)

    while temp > min_temp:
        # Create new neighbor tour
        new_tour = current_tour[:]
        l = random.randint(1, len(new_tour) - 3)
        h = random.randint(l + 1, len(new_tour) - 2)
        new_tour[l:h] = reversed(new_tour[l:h])

        new_cost = calculate_tour_cost(new_tour)
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_tour = new_tour[:]
            current_cost = new_cost

        temp *= cooling_rate

    return current_tour, current_cost

# Solving the tours for all robots
initial_solutions = generate_initial_solution()
final_tours = []
total_costs = []

for tour in initial_solutions:
    optimized_tour, tour_cost = simulated_annealing(tour)
    final_tours.append(optimized_tour)
    total_costs.append(tour_cost)

overall_total_cost = sum(total_costs)

# Output results
for idx, (tour, cost) in enumerate(zip(final_tours, total_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")