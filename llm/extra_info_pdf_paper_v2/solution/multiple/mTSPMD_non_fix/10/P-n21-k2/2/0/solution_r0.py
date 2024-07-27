import math
import random

# Cities coordinates indexed by numbers
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Function to calculate distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initial solution generator
def initial_solution():
    non_depot_cities = list(cities.keys())[2:]  # Exclude depots
    random.shuffle(non_depot_cities)
    return [0] + non_depot_cities[:10] + [0], [1] + non_depot_cities[10:] + [1]

# Calculate the cost of the tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Simulated annealing
def simulated_annealing(initial_tour):
    temperature = 10000
    cooling_rate = 0.995
    current_tour = initial_tour[:]
    current_cost = calculate_cost(current_tour)
    best_tour = current_tour[:]
    best_cost = current_cost

    while temperature > 1:
        new_tour = current_tour[:]
        l = random.randint(1, len(new_tour) - 3)
        r = random.randint(l+1, len(new_tour) - 2)
        new_tour[l:r] = reversed(new_tour[l:r])
        new_cost = calculate_cost(new_tour)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_tour = new_tour
            current_cost = new_cost
            if current_cost < best_cost:
                best_tour = current_tour[:]
                best_cost = current_cost
        
        temperature *= cooling_rate
    
    return best_tour, best_cost

# Main function to solve the problem
def solve():
    tour1, tour2 = initial_solution()
    result_tour1, cost1 = simulated_annealing(tour1)
    result_tour2, cost2 = simulated_annealing(tour2)
    total_cost = cost1 + cost2

    print("Robot 0 Tour:", result_tour1)
    print("Robot 0 Total Travel Cost:", cost1)
    print("\nRobot 1 Tour:", result_tour2)
    print("Robot 1 Total Travel!”

# Entry point
solve()