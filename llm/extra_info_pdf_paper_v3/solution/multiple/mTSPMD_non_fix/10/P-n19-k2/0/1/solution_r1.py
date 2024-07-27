import math
import random

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def simulated_annealing(init_state, distance_matrix, temp=10000, cooling_rate=0.995, min_temp=1):
    current_solution = init_state.copy()
    current_cost = total_distance(current_solution, distance_matrix)
    best_solution = current_solution.copy()
    best_cost = current_cost
    
    while temp > min_temp:
        i, j = sorted(random.sample(range(1, len(current_solution) - 1), 2))
        new_solution = current_solution[:i] + current_solution[i:j+1][::-1] + current_solution[j+1:]
        new_cost = total_distance(new_solution, distance_matrix)
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_solution = new_solution
            current_cost = new_cost
            if new_cost < best_cost:
                best_solution = current_solution
                best_cost = new_cost
        temp *= cooling_rate
    
    return best_solution, best_cost

# Define city coordinates, including depots
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Create distance matrix
distance_matrix = [
    [calculate_distance(city_coords[i], city_coords[j]) for j in range(len(city_coords))]
    for i in range(len(city_coords))
]

# Initial partition of cities among robots
split_index = len(city_coords) // 2
robot_tours = [
    [0] + list(range(1, split_index)),
    [0] + list(range(split_index, len(city_coords)))
]

# Apply Simulated Annealing for each robot
results = []
total_cost = 0

for i, init_tour in enumerate(robot_tours):
    tour, cost = simulated_annealing(init_tour + [0], distance_matrix)  # Each tour starts and ends at Depot 0
    results.append((tour, cost))
    total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")