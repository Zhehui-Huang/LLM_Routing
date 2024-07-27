import numpy as n
from math import sqrt

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p2[1] - p1[1])**2)

# Coordinates for each city
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Supplied robot tours and costs
robot_tours = [
    [0, 17, 15, 12, 9, 8, 4, 0],
    [0, 14, 7, 6, 3, 11, 0],
    [0, 16, 19, 10, 2, 5, 0],
    [0, 1, 13, 21, 20, 18, 0],
]

robot_costs_supplied = [158.09, 124.08, 159.96, 194.91]
max_cost_supplied = 194.91

def test_solution():
    # Validate unique visits to each city and calculate actual travel costs
    all_visited_cities = set()
    calculated_costs = []
    for tour in robot_tours:
        visited_cities_set = set(tour)
        
        # Check if the robots return to the depot
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL")
            return
        
        # Calculate and verify the cost
        tour_cost = 0
        for i in range(len(tour) - 1):
            dist = euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
            tour_cost += dist
        
        calculated_costs.append(round(tour_cost, 2))
        all_visited_cities.update(visited_cities_set)
    
    # Check all cities are visited exactly once
    if len(all_visited_cities) != 22 or any(tour.count(city) > 1 for city in range(1, 22) for tour in robot_tours):
        print("FAIL")
        return
    
    # Check costs match the given costs
    if not all(supplied == calculated for supplied, calculated in zip(robot_costs_supplied, calculated_costs)):
        print("FAIL")
        return
    
    # Check maximum costs
    max_calculated_cost = max(calculated_costs)
    if max_calculated_cost != max_cost_supplied:
        print("FAIL")
        return
    
    print("CORRECT")

# Run the tests
test_solution()