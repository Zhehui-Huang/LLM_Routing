import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_tour_and_cost(cities, tour, expected_cost):
    # Validate if the given coordinates match the description
    if cities[0] != (35, 40):
        return "FAIL"

    # Validate the total number of cities including the depot as described
    if len(cities) != 15:
        return "FAIL"

    # Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are covered exactly once, except the depot that's revisited at the end
    if len(set(tour)) != len(cities):
        return "FAIL"

    # Calculate the total travel cost from the provided tour
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_distance(cities[tour[i-1]], cities[tour[i]])
    
    # Compare the calculated cost with the expected travel cost
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# City coordinates as defined
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Tour and total travel cost given by the solution
tour = [0, 10, 11, 12, 4, 13, 14, 8, 9, 7, 3, 6, 2, 5, 1, 0]
total_travel_cost = 520.7795498520583

# Verify and print the result
result = verify_tour_and_cost(cities, tour, total_travel_cost)
print(result)