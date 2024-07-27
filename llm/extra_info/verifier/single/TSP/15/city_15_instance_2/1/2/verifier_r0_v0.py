import numpy as np

def calculate_euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities, total_travel_cost):
    # Check if the robot starts and ends its journey at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the robot visits each of the cities from 1 to 14 exactly once
    unique_cities = list(range(15)) 
    if sorted(tour) != unique_cities:
        return "FAIL"
    
    # Check if the total cost calculated using Euclidean distance matches the given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1_idx, city2_idx = tour[i], tour[i+1]
        city1, city2 = cities[city1_idx], cities[city2_idx]
        calculated_cost += calculate_euclidean_distance(city1, city2)

    if not np.isclose(calculated_rating_cost, total_travel_cost, rtol=1e-05):
        return "FAIL"

    return "CORRECT"

# Given city coordinates and test tour
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_travel_cost = 322.5037276986899

# Check if the solution is correct
result = verify_solution(tour, cities, total_travel_cost)
print(result)