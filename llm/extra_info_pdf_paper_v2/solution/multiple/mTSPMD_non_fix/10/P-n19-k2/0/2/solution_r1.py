import math
import random

# Define city locations
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Function to compute Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Simulated Annealing algorithm
def simulated_annealing(tour, temp=1000, cooling_rate=0.99, num_iter=1000):
    current_cost = calculate_cost(tour)
    best_tour = tour[:]
    best_cost = current_cost

    for i in range(num_iter):
        temp *= cooling_rate
        new_tour = tour[:]
        a, b = sorted(random.sample(range(1, len(tour)), 2))  # Exclude depot when swapping
        new_tour[a:b] = reversed(new_tour[a:b])  # Reverse slice technique
        
        new_cost = calculate_cost(new_tour)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            tour = new_tour
            current_cost = new_cost
        
            if new_cost < best_cost:
                best_tour = tour[:]
                best_cost = new_cost
    
    return best_tour, best_cost

def calculate_cost(tour):
    return sum(distance(tour[i], tour[(i + 1) % len(tour)]) for i in range(len(tour)))

# Assign non-depot cities to robots
robot0_cities = [0] + list(range(2, 11))  # First half
robot1_cities = [1] + list(range(11, 19))  # Second half

# Optimizing each robot's tour separately
optimized_tour_0, cost_0 = simulated_annealing(robot0_cities)
optimized_tour_1, cost_1 = simulated_annealing(robot1_cities)

overall_cost = cost_0 + cost_1

# Output the tours and costs
print("Robot 0 Tour:", optimized_tour_0)
print("Robot 0 Total Travel Cost:", cost_0)
print()
print("Robot 1 Tour:", optimized_tour_1)
print("Robot 1 Total Travel Cost:", cost_1)
print()
print("Overall Total Travel Cost:", overall_cost)