import math
import random

# Cities coordinates indexed by numbers
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate an initial solution by splitting cities optimally
def initial_solution():
    cities_list = list(cities.keys())[2:]  # Exclude the depots initially
    random.shuffle(cities_list)  # Shuffle non-depot cities
    half_size = len(cities_list) // 2
    return [0] + cities_list[:half_size], [1] + cities_list[half_size:]

# Simulated annealing to find a good path solution
def simulated_annealing(initial_tour):
    temperature = 10000
    cooling_rate = 0.995
    current_tour = initial_tour[:]
    current_cost = calculate_cost(current_tour)

    while temperature > 1:
        # Randomly swap two cities in the tour (excluding the first and last city deps)
        new_tour = current_tour[:]
        l = random.randint(1, len(new_tour) - 2)
        r = random.randint(1, len(new_tour) - 2)
        new_tour[l], new_tour[r] = new_tour[r], new_tour[l]
        new_cost = calculate_cost(new_tour)

        # Acceptance condition or better cost
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_tour = new_tour
            current_cost = new_cost

        temperature *= cooling_rate

    return current_tour, current_cost

# Calculate total cost of the tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

def solve():
    tour1, tour2 = initial_solution()
    result_tour1, cost1 = simulated_annealing(tour1)
    result_tour2, cost2 = simulated_annealing(tour2)
    total_cost = cost1 + cost2
    
    print("Robot 0 Tour:", result_tour1)
    print("Robot 0 Total Travel Cost:", cost1)
    print("\nRobot 1 Tour:", result_tour2)
    print("Robot 1 Total Travel Cost:", cost2)
    print("\nOverall Total Travel Cost:", total_cost)

solve()