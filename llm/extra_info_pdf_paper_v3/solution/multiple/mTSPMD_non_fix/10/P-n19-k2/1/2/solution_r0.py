import numpy as np
import random
import math

# City and coordinate information
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

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initial random solution generator
def generate_initial_solution():
    all_cities = list(range(2, len(cities)))  # inherently excluding depot cities
    random.shuffle(all_cities)
    split = len(all_cities) // 2
    return all_cities[:split], all_cities[split:]

# Total cost of a tour
def calculate_total_cost(tour, starting_depot):
    cost = euclidean_distance(starting_depot, tour[0])
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i - 1], tour[i])
    return cost

# Simulated Annealing algorithm to optimize tour
def simulated_annealing(initial_tour, depot, temperature=10000, cooling_rate=0.995, stopping_temp=1):
    current_tour = initial_tour.copy()
    best_tour = initial_tour.copy()
    current_cost = calculate_total_cost(current_tour, depot)
    best_cost = current_cost
    
    while temperature > stopping_temp:
        next_tour = current_tour.copy()
        l = random.randint(1, len(next_tour) - 2)
        i = random.randint(0, len(next_tour) - l)
        next_tour[i : (i + l)] = reversed(next_tour[i : (i + l)])
        
        next_cost = calculate_total_cost(next_tour, depot)
        if next_cost < current_cost or random.random() < np.exp((current_cost - next_cost) / temperature):
            current_tour, current_cost = next_tour, next_cost
            
            if current_cost < best_cost:
                best_tour, best_cost = current_tour, current_cost
        
        temperature *= cooling_rate

    return best_tour, best_cost

# Solve the problem
def solve_problem():
    tour1, tour2 = generate_initial_solution()
    tour1, cost1 = simulated_annealing(tour1, 0)
    tour2, cost2 = simulated_annealing(tour2, 1)
    overall_cost = cost1 + cost2
    
    print("Robot 0 Tour: [0,", ', '.join(map(str, tour1)), ", 0]")
    print("Robot 0 Total Travel Cost:", cost1)
    print("Robot 1 Tour: [1,", ', '.join(map(str, tour2)), ", 1]")
    print("Robot 1 Total Travel Cost:", cost2)
    print("\nOverall Total Travel Cost:", overall_cost)

solve_problem()