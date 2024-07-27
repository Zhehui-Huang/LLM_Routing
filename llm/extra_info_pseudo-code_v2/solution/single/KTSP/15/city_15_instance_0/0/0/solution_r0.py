import random
import math
from itertools import permutations

# Define the cities
cities = {
    0: (9, 93), 
    1: (8, 51), 
    2: (74, 99), 
    3: (78, 50), 
    4: (21, 23), 
    5: (88, 59), 
    6: (79, 77), 
    7: (63, 23), 
    8: (19, 76), 
    9: (21, 38), 
    10: (19, 65), 
    11: (11, 40), 
    12: (3, 21), 
    13: (60, 55), 
    14: (4, 39)
}

# Define the Euclidean distance calculator
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Neighborhood structures
def swap(cities_list):
    len_cities = len(cities_list)
    best_tour = cities_list[:]
    best_cost = calculate_total_distance(best_tour)
    for i in range(1, len_cities-1):
        for j in range(i+1, len_cities-1):
            new_tour = cities_list[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = calculate_total_distance(new_tour)
            if new_cost < best_cost:
                best_tour = new_tour
                best_cost = new_cost
    return best_tour

# Calculate the travel cost of a tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    return total_distance

# General Variable Neighborhood Search Algorithm
def GVNS(k, max_iter=1000):
    best_tour = generate_initial_solution(k)
    best_cost = calculate_total_distance(best_tour)
    
    for _ in range(max_iter):
        current_tour = shake(best_tour)
        local_tour = VND(current_tour)
        local_cost = calculate_total_distance(local_tour)
        
        if local_cost < best_cost:
            best_tour = local_tour
            best_cost = local_cost
    
    return best_tour, best_cost

# Generating the initial solution
def generate_initial_solution(k):
    tour = [0]
    while len(tour) < k:
        possible_cities = list(set(range(1, len(cities))) - set(tour))
        city = random.choice(possible_cities)
        tour.append(city)
    tour.append(0)
    return tour

# Random shake function to generate new initial points
def shake(tour):
    mid_tour = tour[1:-1]
    random.shuffle(mid_tour)
    return [0] + mid_tour + [0]

# Variable Neighborhood Descent
def VND(tour):
    improved = True
    while improved:
        new_tour = swap(tour)
        if new_tour != tour:
            tour = new_tour
        else:
            improved = False
    return tour

# Main execution
if __name__ == "__main__":
    k = 4  # Number of cities to visit (including depot)
    result_tour, result_cost = GVNS(k)
    print("Tour:", result_tour)
    print("Total travel cost:", round(result_cost, 2))