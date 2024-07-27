import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, total_cost):
    city_coordinates = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
        (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
        (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
        (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]

    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly 16 cities, including the depot city
    if len(set(tour)) != 16:
        return "FAIL"

    # Check tour length calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])

    # Requirement 3: Check if the total travel cost matches the calculated cost
    if not math.isclose(total_cost, calculated_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 0]
total_travel_cost = 285.96

# Validate tour
result = validate_tour(tour, total_travel_cost)
print(result)