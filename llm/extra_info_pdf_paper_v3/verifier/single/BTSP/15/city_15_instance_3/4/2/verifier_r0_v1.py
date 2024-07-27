import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities):
    # Verify the tour begins and ends at the depot, and each city is visited once
    if tour[0] != 0 or tour[-1] != 0:
        return False
    if sorted(tour) != sorted(list(range(len(cities)))):
        return False
    return True

def verify_total_and_max_distance(tour, cities, total_cost, max_distance):
    calculated_total_cost = 0
    calculated_max_distance = 0
    # Calculate the travel cost and max distance
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    # Verify against provided values
    if not (math.isclose(calculated_total_cost, total_cost, abs_tol=1e-2) and 
            math.isclose(calculated_max_distance, max_distance, abs_tol=1e-2)):
        return False
    return True

# Provided solution
tour = [0, 14, 1, 4, 12, 3, 7, 5, 9, 10, 13, 6, 8, 11, 2, 0]
total_cost = 389.24
max_distance = 94.11
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Check requirements
if verify_tour(tour, cities) and verify_total_and_max_distance(tour, cities, total_cost, max_robotanistance):
    print("CORRECT")
else:
    print("FAIL")