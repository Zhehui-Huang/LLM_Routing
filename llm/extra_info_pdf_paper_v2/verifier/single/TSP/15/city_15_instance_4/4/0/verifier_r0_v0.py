import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour_and_cost(tour, total_cost, cities):
    # Test if the tour starts and ends at the depot city (Requirement 3)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test if all cities are visited exactly once except the depot (Requirement 1)
    visits = set(tour)
    if len(visits) != len(cities) or set(range(len(cities))) != visits:
        return "FAIL"
    
    # Calculate the total travel cost and compare (Requirement 2 & 4)
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    if round(calculated_cost, 1) != round(total_cost, 1):  # rounding for floating-point precision handling
        return "FAIL"
    
    # If all tests are passed:
    return "CORRECT"

# Define the cities coordinates
cities = [
    (35, 40),  # Depot
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

# Provided tour and total cost
tour = [0, 10, 13, 14, 3, 8, 6, 12, 11, 4, 7, 2, 9, 5, 1, 0]
total_cost = 334.4

# Call the verification function
result = verify_tour_and_cost(tour, total_cost, cities)
print(result)