import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def is_tour_valid(tour, num_cities):
    if tour[0] == 0 and tour[-1] == 0:
        return len(set(tour) - {0}) == num_cities - 1
    return False

def calculate_total_distance(tour, coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_distance

def check_solution():
    coordinates = [
        (79, 15), # Depot city 0
        (79, 55), # City 1
        (4, 80),  # City 2
        (65, 26), # City 3
        (92, 9),  # City 4
        (83, 61), # City 5
        (22, 21), # City 6
        (97, 70), # City 7
        (20, 99), # City 8
        (66, 62)  # City 9
    ]
    # The provided tour and cost
    provided_tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
    provided_total_cost = 320.7939094250147
    
    if not is_tour_valid(provided_tour, len(coordinates)):
        return "FAIL"
    
    calculated_total_cost = calculate_total_distance(provided_tour, coordinates)
    
    # Allow a small margin for floating point arithmetic differences and rounding errors
    if abs(calculated_total_cost - provided_total_cost) > 1e-6:
        return "FAIL"
    
    return "CORRECT"

# Execute the test
test_result = check_solution()
print(test_result)