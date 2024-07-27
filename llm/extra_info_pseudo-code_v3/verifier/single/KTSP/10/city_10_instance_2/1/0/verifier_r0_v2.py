import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tour, provided_total_cost):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 6 cities are visited (including repeating the depot city)
    if len(tour) != 7:  # 6 cities including 0, and returning to 0
        return "FAIL"
    
    # Check if the tour only contains valid city indices
    if any(city < 0 or city >= len(cities) for city in tour):
        return "FAIL"

    # Calculate the total travel cost based on submitted tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Compare the provided cost with the calculated cost
    if not math.isclose(provided_total_cost, calculated_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Coordinates for each of the 10 cities
cities = [
    (90, 3),  # City 0 - Depot
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Tour and cost provided in your solution output
tour = [0, 9, 1, 5, 8, 0]
total_travel_cost = 174.69223764340376

# Call the verification function
result = verify_solution(cities, tour, total_travel_db_cost)
print(result)