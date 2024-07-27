import math
import random

# City coordinates including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69),
    18: (45, 35)
}

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities given their coordinates."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(tour):
    """Calculate the total distance of a tour."""
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def simulated_annealing(cities, depot, non_depot_cities, num_iterations=10000, start_temp=100, alpha=0.99):
    """Perform the Simulated Annealing algorithm to find an optimal tour from the given depot."""
    # Generate an initial random tour from the depot
    tour = [depot] + random.sample(non_depot_cities, len(non_depot_cities))
    
    current_dist = total_distance(tour + [depot])
    best_tour = tour[:]
    best_dist = current_dist
    temp = start_temp
    
    for _ in range(num_iterations):
        # Cooling down
        temp *= alpha
        
        # Swap two cities
        idx1, idx2 = random.randint(1, len(tour) - 1), random.randint(1, len(tour) - 1)
        tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
        
        new_dist = total_distance(tour + [depot])
        
        # Decide whether to accept the new tour
        if new_dist < current_dist or random.random() < math.exp((current_dist - new_dist) / temp):
            current_dist = new_dist
            if current_dist < best_dist:
                best_tour = tour[:]
                best_dist = current_dist
        else:
            # Revert swap
            tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
    
    return best_tour, best_dist

# Separate city indices for depot
depot_0 = 0
depot_1 = 1
non_depot_cities = [i for i in cities if i not in [depot_0, depot_1]]

# Run simulated annealing for both robots
robot_0_tour, robot_0_cost = simulated_annealing(cities, depot_0, non_depot_cities)
robot_1_tour, robot_1_cost = simulated_annealing(cities, depot_1, non_depot_cities)

# Output the results
print(f"Robot 0 Tour: {[depot_0] + robot_0_tour + [depot_0]}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost:.2f}\n")
print(f"Robot 1 Tour: {[depot_1] + robot_1_tour + [depot_1]}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost:.2f}\n")

# Total cost for all robots
overall_total_cost = robot_0_cost + robot_1_cost
print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")