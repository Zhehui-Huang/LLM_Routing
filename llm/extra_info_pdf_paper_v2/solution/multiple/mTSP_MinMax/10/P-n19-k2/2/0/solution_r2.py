import math
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate Euclidean distance between two cities
def dist(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Variable Neighborhood Search to optimize initial good solution
def variable_neighborhood_search(init_tours):
    def swap_cities(tour):
        i, j = random.sample(range(1, len(tour)-1), 2)
        tour[i], tour[j] = tour[j], tour[i]
        return tour

    def calculate_cost(tour):
        return sum(dist(tour[i], tour[i+1]) for i in range(len(tour)-1))

    best_tours = init_tours[:]
    best_cost = max(calculate_cost(tour) for tour in best_tours)

    for _ in range(1000):  # Max iterations
        new_tours = [swap_cities(tour[:]) for tour in best_tours]
        new_cost = max(calculate_cost(tour) for tour in new_tours)
        
        if new_cost < best_cost:
            best_tours, best_cost = new_tours, new_cost

    return best_tours, best_cost

# Distribute cities to robots with initial greedy approach
def distribute_cities(num_robots):
    all_cities = list(cities.keys())[1:]  # Exclude depot (city 0)
    random.shuffle(all_cities)
    chunks = [all_cities[i::num_robots] for i in range(num_robots)]
    tours = [[0] + chunk + [0] for chunk in chunks]  # Start and end at depot
    return tours

# Run the heuristic solver
def solve_mTSP(num_robots):
    initial_tours = distribute_cities(num_robots)
    optimized_tours, max_travel_cost = variable_neighborhood_search(initial_tours)
    
    # Display results
    for i, tour in enumerate(optimized_tours):
        tour_cost = sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost}")
        
    print("Maximum Travel Cost:", max_travel_cost)

# Example of solving for 2 robots
solve_mTSP(2)