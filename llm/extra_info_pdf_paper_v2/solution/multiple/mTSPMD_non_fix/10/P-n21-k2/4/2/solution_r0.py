import random
import math

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35)
}

# Function to calculate euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Simulated Annealing function to minimize the tour costs
def simulated_annealing(initial_state):
    temp = 5000
    alpha = 0.99
    min_temp = 1
    current_state = initial_state
    current_cost = calculate_total_cost(current_state)

    while temp > min_temp:
        next_state = get_neighbour(current_state)
        next_cost = calculate_total_cost(next_data)
        cost_diff = next_cost - current_cost

        if cost_diff < 0 or math.exp(-cost_diff / temp) > random.random():
            current_state, current_cost = next_state, next_cost
        
        temp *= alpha

    return current_state, current_cost

# Function to calculate total cost for a given solution
def calculate_total_cost(state):
    total_cost = 0
    for tour in state:
        tour_cost = 0
        for i in range(len(tour)-1):
            tour_cost += euclidean_distance(tour[i], tour[i+1])
        total_cost += tour_cost
    return total_cost

# Function to generate neighbour state by slightly modifying existing tours
def get_neighbour(state):
    new_state = [tour[:] for tour in state]
    tour_index = random.randint(0, len(new_state) - 1)
    if len(new_state[tour_index]) > 2:  # Ensure there are at least two cities to swap
        i, j = random.sample(range(1, len(new_state[tour_index])-1), 2)
        new_state[tour_index][i], new_state[tour_index][j] = new_state[tour_index][j], new_state[tour_index][i]
    return new_state

# Initial solution: Distribute cities between two robots
robot_0_cities = [0, 2, 3, 6, 7, 10, 12, 16]
robot_1_cities = [1, 4, 5, 8, 9, 13, 14, 17, 18, 19, 20]
initial_state = [robot_0_cities[:], robot_1_cities[:]]

best_tours, best_cost = simulated_annealing(initial_state)

# Print the results
overall_total_cost = 0
for idx, tour in enumerate(best_tours):
    tour_cost = 0
    for i in range(len(tour)-1):
        tour_cost += euclidean_distance(tour[i], tour[i+1])
    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")