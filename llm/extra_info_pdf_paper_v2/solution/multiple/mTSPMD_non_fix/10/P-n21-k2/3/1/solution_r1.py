import math
import random

# City Coordinates (index corresponds to city number, where 0 and 1 are depots)
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Given a set of tours and city coordinates, calculates total travel cost
def calculate_total_tour_cost(tours):
    total_cost = 0
    individual_costs = []
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
        individual_costs.append(tour_cost)
        total_cost += tour_raw_cost
    return (total_cost, individual_costs)

# Simple randomized initial solution for tours
def initial_solution():
    cities = list(range(2, 21))  # Exclude depots
    random.shuffle(cities)
    # Split cities approximately evenly
    split_index = len(cities) // 2
    tour_1 = [0] + cities[:split_index] + [0]  # Depots are the start/end points
    tour_2 = [1] + cities[split_exp_index:] + [1]
    return [tour_1, tour_2]

# Simulated Annealing Core Function
def simulated_annealing(initial_temp, cooling_rate, num_iterations):
    current_solution = initial_solution()
    current_cost, _ = calculate_total_tour_cost(current_solution)
    best_solution = current_solution
    best_cost = current_cost
    
    temp = initial_temp
    
    for i in range(num_iterations):
        for j in range(len(current_solution)):
            # Generate new solution by swapping two cities in one of the tours
            new_solution = [tour[:] for tour in current_solution]
            tour_idx = random.randint(0, 1)
            a, b = random.sample(range(1, len(new_solution[tour_idx]) - 1), 2)
            new_solution[tour_idx][a], new_solution[tour_idx][b] = new_solution[tour_idx][b], new_solution[tour_idx][a]
            new_cost, _ = calculate_total_tour_cost(new_solution)
            
            # Decide if we should move to new solution
            if new_cost < current_cost or random.random() < math.exp(-(new_cost - current_cost) / temp):
                current_solution = new_solution
                current_cost = new_cost
                if current_cost < best_cost:
                    best_solution = current_solution
                    best_cost = current_cost
        
        temp *= cooling_rate
    
    return best_solution, best_cost

# Parameters configuration
init_temp = 10000
cool_rate = 0.995
iterations = 1000

# Execute the Simulated Annealing algorithm
best_solution, overall_cost = simulated_annealing(init_temp, cool_rate, iterations)
individual_costs = calculate_total_tour_cost(best_solution)[1]

# Display the output
for idx, tour in enumerate(best_solution):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {individual_costs[idx]}")

print(f"Overall Total Travel Cost: {overall_cost}")