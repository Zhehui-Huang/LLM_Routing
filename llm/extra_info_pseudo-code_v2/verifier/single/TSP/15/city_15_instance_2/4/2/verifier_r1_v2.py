import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost, city_coordinates):
    # Check that the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check that each city is visited exactly once
    if len(set(tour)) != len(tour):
        return "FAIL"
    
    # Check that the tour includes all cities
    all_cities = set(range(len(city_coordinates)))
    tour_cities = set(tour)
    if tour_cities != all_cities:
        return "FAIL"
    
    # Calculate the total travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        x1, y1 = city_coordinates[city_from]
        x2, y2 = city_coordinates[city_to]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Compare the provided cost with the calculated cost
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-3):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates based on given details
city_coordinates = {0: (54, 87),  1: (21, 84),  2: (69, 84),
                    3: (53, 40),  4: (54, 42),  5: (36, 30),
                    6: (52, 82),  7: (93, 44),  8: (21, 78),
                    9: (68, 14), 10: (51, 28), 11: (44, 79),
                    12: (56, 58), 13: (72, 43), 14: (6, 99)}

# Tour and cost to be validated
tour = [0, 2, 7, 13, 4, 5, 10, 9, 3, 12, 11, 14, 1, 8, 6, 0]
total_travel_cost = 339.03

# Execute the unit test
result = verify_solution(tour, total_travel_cost, city_coordinates)
print("Test result:", result)