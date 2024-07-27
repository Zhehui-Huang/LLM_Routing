import math
import random

# City coordinates provided
coordinates = [
    (9, 93),   # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

def euclidean_distance(c1, c2):
    """ Calculate Euclidean distance between two cities based on given indices """
    return math.sqrt((coordinates[c1][0] - coordinates[c2][0]) ** 2 + (coordinates[c1][1] - coordinates[c2][1]) ** 2)

def validate_route(route):
    """ Calculate the total distance of the route and find max distance between consecutive cities """
    total_cost = 0
    max_distance = 0
    for i in range(len(route) - 1):
        distance = euclidean_distance(route[i], route[i + 1])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return total_cost, max_distance

def simulated_annealing():
    """ Simulated Annealing to minimize the longest distance between any two consecutive cities in the route """
    # Start the initial route: 0 -> 1 -> 2 -> ... -> 14 -> 0
    current_route = list(range(15)) + [0]
    current_cost, current_max = validate_route(current_route)
    
    temperature = 100
    cooling_rate = 0.995
    min_temperature = 0.01
    
    while temperature > min_temperature:
        # Generate a new candidate solution
        new_route = current_route[:]
        middle = new_route[1:-1]
        random.shuffle(middle)
        new_route[1:-1] = middle
        new_cost, new_max = validate_route(new_route)
        
        # Decision to accept the new solution
        if new_max < current_max or random.uniform(0, 1) < math.exp((current_max - new_max) / temperature):
            current_route, current_cost, current_max = new_route, new_cost, new_max
            
        # Cool down the system
        temperature *= cooling_rate

    return current_route, current_cost, current_max

# Running the simulated annealing
tour, total_travel_cost, max_distance_between_cities = simulated_annealing()

# Outputting the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_between_cities)