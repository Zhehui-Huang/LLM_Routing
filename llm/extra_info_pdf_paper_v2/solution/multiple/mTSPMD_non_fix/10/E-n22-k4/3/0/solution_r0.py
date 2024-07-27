import math
import random

# City coordinates: City index is the key and coordinates (tuple) are the values
city_coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Function to calculate Euclidean distance between two cities
def distance(city1_index, city2_index):
    x1, y1 = city_coordinates[city1_index]
    x2, y2 = city_coordinates[city2_index]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Simulated Annealing utility functions
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i+1])
    return total_cost

def swap_two_cities(tour):
    idx1, idx2 = random.sample(range(1, len(tour)), 2)  # Avoid swapping the depot city
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
    return tour

def simulated_annealing(initial_tour, initial_temp, cooling_rate, stopping_temp):
    current_temp = initial_temp
    current_tour = initial_tour[:]
    current_cost = calculate_cost(current_tour)
    best_tour = current_tour[:]
    best_cost = current_cost

    while current_temp > stopping_temp:
        new_tour = swap_two_cities(current_tour[:])
        new_cost = calculate_cost(new_tour)
        cost_delta = new_cost - current_cost

        if cost_delta < 0 or random.random() < math.exp(-cost_delta / current_temp):
            current_tour = new_tour
            current_cost = new_cost
            
            if new_cost < best_cost:
                best_tour = new_tour
                best_cost = new_cost

        current_temp *= (1 - cooling_rate)
    
    return best_tour, best_cost

# Prepare robot tours
depot = 0
cities = list(city_coordinates.keys())
cities.remove(depot)
initial_tour = [depot] + cities + [depot]

temp, cooling_rate, stop_temp = 10000, 0.003, 1
final_tour, final_cost = simulated_annealing(initial_tour, temp, cooling_rate, stop_temp)

print(f"Robot 0 Tour: {final_tour}")
print(f"Robot 0 Total Travel Cost: {final_cost}")
print(f"Overall Total Travel Cost: {final_cost}")