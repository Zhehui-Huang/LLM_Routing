import math
import random

# City Coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Distances between each pair of cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Simulated Annealing Setup
def simulated_annealing(tour, initial_temp, cooling_rate, num_iterations):
    current_temp = initial_temp
    current_tour = tour[:]
    current_cost = total_tour_cost(current_tour)
    
    def total_tour_cost(tour):
        return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    best_tour = current_tour[:]
    best_cost = current_cost
    
    for i in range(num_iterations):
        next_tour = current_tour[:]
        # Make a swap
        l = random.randint(1, len(next_tour) - 2)
        r = random.randint(1, len(next_tour) - 2)
        next_tour[l], next_tour[r] = next_tour[r], next_tour[l]
        next_cost = total_tour_cost(next_tour)
        
        # Acceptance probability
        if next_cost < current_cost or random.random() < math.exp((current_cost - next_cost) / current_temp):
            current_tour = next_tour[:]
            current_cost = next_cost
            
            if current_cost < best_cost:
                best_tour = current_tour[:]
                best_cost = current_cost
                
        current_temp *= cooling_rate
    
    return best_tour, best_cost

# Setup robots starting from depot 0
robots = 4
cities_per_robot = len(cities) // robots
assignments = [list(range(i * cities_per_robot, (i + 1) * cities_per_robot)) for i in range(robots)]

tours = []
costs = []

for i in range(robots):
    tour, cost = simulated_annealing([0] + assignments[i], initial_temp=100, cooling_rate=0.995, num_iterations=1000)
    tours.append(tour)
    costs.append(cost)

total_cost = sum(costs)

# Output results
for i in range(robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {total_cost}")