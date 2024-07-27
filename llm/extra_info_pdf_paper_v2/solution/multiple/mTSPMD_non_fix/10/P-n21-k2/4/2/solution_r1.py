import random
import math

# Coordinates for each city, including the depots.
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35)
}

# Euclidean distance calculation between two cities
def euclidean_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate a random solution with given groups of cities for each robot
def generate_initial_solution():
    all_cities = list(cities.keys())[2:]  # exclude depots
    random.shuffle(all_cities)
    mid_point = len(all_cities) // 2
    return [all_cities[:mid_point], all_cities[mid_point:]]

# Simulated Annealing for optimization
def simulated_annealing(initial_state):
    temp = 10000
    alpha = 0.995
    min_temp = 1
    current_state = initial_state
    current_cost = calculate_total_cost(current_state)

    while temp > min_temp:
        neighbor = get_neighbour(current_state)
        neighbor_cost = calculate_total_cost(neighbor)
        
        if neighbor_cost < current_cost or random.random() < math.exp(-(neighbor_cost - current_cost) / temp):
            current_state, current_cost = neighbor, neighbor_cost
        
        temp *= alpha

    return current_state, current_cost

# Calculate total cost of tours
def calculate_total_cost(state):
    total_cost = 0
    for tour in state:
        tour_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        total_cost += tour_cost
    return total_cost

# Generate a neighboring state
def get_neighbour(state):
    tour_index = random.randint(0, 1)
    tour = state[tour_index]
    if len(tour) > 2:  # At least 3 cities to perform a swap
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return state

# Initial solution and solving by Simulated Annealing
initial_state = [generate_initial_solution(), generate_initial_solution()]
best_tours, best_cost = simulated_annealing(initial_state)

# Print the results
overall_total_cost = 0
for idx, tour in enumerate(best_tours):
    # Include depot at the beginning and best end-city for each robot
    tour = [idx] + tour
    tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel asistance: {round(tour_cost, 2)}")

print(f"Overall Total Cost: {round(overall_total_cost, 2)}")