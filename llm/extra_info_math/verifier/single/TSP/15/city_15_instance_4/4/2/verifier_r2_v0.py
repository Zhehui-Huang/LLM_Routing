import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, coordinates, reported_cost):
    # Requirement 1: Start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city visited exactly once (aside from the depot city)
    visited_cities = set(tour)
    if len(visited_cities) != len(coordinates) or any(city not in visited_cities for city in range(len(coordinates))):
        return "FAIL"
    
    # Requirement 3 and 4: Calculate the total travel cost and compare
    total_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        total_cost += calculate_distance(coordinates[city_from][0], coordinates[city_from][1], coordinates[city_to][0], coordinates[city_to][1])
    if round(total_cost, 2) != round(reported_cost, 2):
        return "FAIL"
    
    return "CORRECT"

# Coordinates from the problem statement including the depot city and other cities
coordinates = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# The tour and total cost reported from the solution
tour_reported = [0, 1, 5, 9, 2, 7, 4, 12, 11, 6, 3, 8, 14, 13, 10, 0]
total_cost_reported = 288.52

# Verify the solution
verification_result = verify_solution(tour_reported, coordinates, total_cost_reported)
print(verification_result)