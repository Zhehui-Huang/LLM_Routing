import math
import random

# Cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Simulated Annealing parameters
T = 1000  # Initial temperature
cooling_rate = 0.95
min_temp = 1
num_iteration = 500

def tour_cost(tour):
    cost = 0
    for i in range(len(tour)-1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

def simulated_annealing(depot):
    # Create initial tour from the depot
    tour = [depot] + [city for city in cities.keys() if city != depot]
    current_cost = tour_cost(tour)
    
    T = 1000  # Reset temperature for each robot
    while T > min_temp:
        for _ in range(num_iteration):
            # Make a swap (randomly select two indices to swap)
            i, j = sorted(random.sample(range(1, len(tour)), 2))
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]

            new_cost = tour_cost(new_tour)
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
                tour, current_cost = new_tour, new_cost
        
        T *= cooling_rate
    
    return tour, current_cost

# Running Simulated Annealing for both robots
robot_0_tour, robot_0_cost = simulated_annealing(0)
robot_1_tour, robot_1_cost = simulated_annealing(1)

# Display Results
print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {round(robot_0_cost, 2)}\n")
print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {round(robot_1_cost, 2)}\n")
overall_cost = robot_0_cost + robot_1_cost
print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")