import math
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates
coordinates = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Groups of cities
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def simulated_annealing(groups, coordinates):
    current_solution = [0] + [random.choice(group) for group in groups] + [0]
    current_cost = calculate_tour_cost(current_solution)
    
    T = 1000  # Initial temperature
    cooling_rate = 0.995
    min_temperature = 0.01
    
    while T > min_temperature:
        new_solution = current_solution[1:-1]
        group_index = random.randint(0, len(groups) - 1)
        new_solution[group_index] = random.choice(groups[group_index])
        
        new_solution = [0] + new_solution + [0]
        new_cost = calculate_tour_cost(new_solution)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
            current_solution = new_solution
            current_cost = new_cost
            
        T *= cooling_rate
    
    return current_solution, current_cost

# Finding the shortest tour using simulated annealing
tour, total_cost = simulated_annealing(groups, coordinates)

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")