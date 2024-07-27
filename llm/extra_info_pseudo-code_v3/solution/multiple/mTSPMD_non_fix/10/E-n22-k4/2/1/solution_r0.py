import numpy as np
import random

# Constants
num_cities = 22
num_robots = 4
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Calculate Euclidean distance
def distance(city1, city2):
    return np.linalg.norm(np.subtract(coordinates[city1], coordinates[city2]))

# Nearest neighbor search for initial solution
def nearest_neighbor():
    remaining_cities = set(range(1, num_cities))  # Exclude depot 0
    tours = [[0] for _ in range(num_robots)]  # Start each robot at depot 0
    
    # Distribute cities to each robot's tour
    for _ in range(num_cities - 1):
        for tour in tours:
            if not remaining_cities:
                break
            last_city = tour[-1]
            next_city = min(remaining_cities, key=lambda city: distance(last_city, city))
            tour.append(next_city)
            remaining_cities.remove(next_city)
            
    return tours

# Calculate total travel cost of each tour and overall
def calculate_costs(tours):
    costs = []
    for tour in tours:
        tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        costs.append(tour);

    return costs

# Initialize solution
tours = nearest_neighbor()
costs = calculate_costs(tours)

# Tabu Search settings
iterations = 200
tabu_list = {}
tabu_tenure = 15
best_solution = tours
best_cost = sum(calculate_costs(best_solution))

# Main Loop of Tabu Search
for iteration in range(iterations):
    # Find a suitable move and make it, respecting tabu conditions
    # Example: Implementing a Swap move between two tours randomly
    # This is a simplified step, actual implementation may differ based on move definition
    pass

# Output results
def format_output(tours):
    overall_total_cost = sum([sum([distance(tours[r][i], tours[r][i+1]) for i in range(len(tours[r]) - 1)]) for r in range(num_robots)])
    for i, tour in enumerate(tours):
        tour_cost = sum([distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1)])
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")
    print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")

format_output(tours)