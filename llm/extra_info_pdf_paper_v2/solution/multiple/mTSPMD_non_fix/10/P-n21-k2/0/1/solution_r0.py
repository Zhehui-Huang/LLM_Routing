import math
import random

# Given cities and coordinates
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
          (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
          (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
          (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Function to calculate Euclidean distance between cities
def euclidean_distance(city1, city2):
    return math.sqrt((coords[city1][0] - coords[city2][0])**2 + (coords[city1][1] - coords[city2][1])**2)

# Simulated Annealing Algorithm
def simulated_annealing():
    # Initialize with a random solution
    cities = list(range(2, 21))  # Cities excluding depots
    random.shuffle(cities)
    partition = random.randint(1, len(cities) - 1)
    route0 = [0] + cities[:partition]
    route1 = [1] + cities[partition:]
    
    def total_cost(route):
        cost = 0
        for i in range(len(route) - 1):
            cost += euclidean_distance(route[i], route[i + 1])
        return cost

    # Initial solution cost
    cost0 = total_cost(route0)
    cost1 = total_cost(route1)
    
    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    while T > T_min:
        i = random.randint(0, len(route0) - 1)
        j = random.randint(0, len(route1) - 1)

        new_route0 = route0[:i] + [route1[j]] + route0[i+1:]
        new_route1 = route1[:j] + [route0[i]] + route1[j+1:]

        new_cost0 = total_cost(new_route0)
        new_cost1 = total_cost(new_route1)
        
        if (new_cost0 + new_cost1 < cost0 + cost1):
            route0 = new_route0
            route1 = new_route1
            cost0 = new_cost0
            cost1 = new_cost1
        else:
            # Probability to accept the worse solution
            if (random.random() < math.exp(-(new_cost0 + new_cost1 - cost0 - cost1) / T)):
                route0 = new_route0
                route1 = new_route1
                cost0 = new_cost0
                cost1 = new_cost1
        T *= alpha
        
    return route0, cost0, route1, cost1

# Run the algorithm
route0, cost0, route1, cost1 = simulated_annealing()

# Print the outputs
print(f"Robot 0 Tour: {route0}")
print(f"Robot 0 Total Travel Cost: {cost0}")

print(f"Robot 1 Tour: {route1}")
print(f"Robot 1 Total Travel Cost: {cost1}")

print(f"Overall Total Travel Cost: {cost0 + cost1}")