import math
import random

# City coordinates definition
city_coords = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Utility function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# Simulated Annealing Functions
def generate_initial_solution(cities):
    """ Generates a random initial solution (tour) by shuffling the city indices """
    tour = cities[:]
    random.shuffle(tour)
    return tour

def calculate_total_distance(tour):
    """ Calculates the total distance of the given tour """
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += euclidean_distance(tour[i], tour[i+1])
    return total_dist

def simulated_annealing(tour, initial_temp, cooling_rate, end_temp):
    """ Performs the simulated annealing optimization """
    temp = initial_temp  # Start temperature
    current_solution = tour
    current_cost = calculate_total_distance(current_solution)
    best_solution = current_solution[:]
    best_cost = current_cost
    
    while temp > end_temp:
        for i in range(100):  # Vary number of iterations per temperature step for performance tuning 
            # Create new neighbour tour
            new_solution = current_solution[:]
            a, b = random.sample(range(1, len(new_solution)), 2)
            new_solution[a], new_solution[b] = new_solution[b], new_solution[a]
            new_cost = calculate_total_distance(new_solution)

            # Decide whether to accept the new solution
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                current_solution = new_solution[:]
                current_cost = new_cost

                if current_cost < best_cost:
                    best_cost = current_cost
                    best_solution = current_solution[:]
                    
        temp *= cooling_rate  # Cool down

    return best_solution, best_cost

# Start planning the tours
num_robots = 4
cities_per_robot = len(city_coords) - 1  # excluding the depot in this case as all start at depot 0

# All cities except depot
cities = list(city_coords.keys())[1:]  # Exclude depot city 0

# Perform optimization
tour, tour_cost = simulated_annealing(cities, initial_temp=1000, cooling_rate=0.995, end_temp=1)

# Output results
print(f"Robot Tour: [0, {' -> '.join(map(str, tour))}]")
print(f"Robot Total Travel Cost: {tour_cost}")

overall_cost = tour_cost  # Since we're planning for only one robot in this demonstration
print(f"Overall Total Travel Cost: {overall_cost}")