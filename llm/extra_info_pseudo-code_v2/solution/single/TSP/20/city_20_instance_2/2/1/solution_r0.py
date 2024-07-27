import math
import random

# Definitions of all cities
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56), 
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53), 
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49), 
    17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the total travel cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Create an initial nearest neighbor tour
def nearest_neighbor_tour(start_city):
    tour = [start_city]
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda c: distance(current_city, c))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # make it a closed tour
    return tour

# Initial tour with nearest neighbor algorithm
initial_tour = nearest_neighbor_tour(0)
initial_cost = tour_cost(initial_tour)

# Function to perform two-opt swap
def two_opt_swap(tour, i, j):
    new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
    return new_tour

# Simulated Annealing to improve the tour
def simulated_annealing(tour, initial_cost):
    current_cost = initial_cost
    current_tour = tour[:]
    T = 100  # initial temperature
    cooling_rate = 0.99
    min_temp = 1e-6
    
    while T > min_temp:
        i, j = sorted(random.sample(range(1, len(cities) - 1), 2))
        new_tour = two_opt_swap(current_tour, i, j)
        new_cost = tour_cost(new_tour)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
            current_tour = new_tour
            current_cost = new_cost
        
        T *= cooling_rate
    
    return current_tour, current_cost

# Perform optimization
final_tour, final_cost = simulated_annealing(initial_tour, initial_cost)

# Results
print("Tour:", final_tour)
print("Total travel cost:", final_cost)

# Generating a safer output
final_result = {
    "Tour": final_tour,
    "Total travel cost": final_cost
}