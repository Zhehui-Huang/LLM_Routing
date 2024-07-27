import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def evaluate_tour(tour, city_coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = city_coordinates[city1]
        x2, y2 = city_coordinates[city2]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    return total_cost

def test_solution():
    city_coordinates = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]
    total_cities = len(city_coordinates)
    initial_tour = [0, 3, 2, 7, 9, 0]
    initial_cost = 331.07347000075094
    
    # Check if tour starts and ends at depot city 0
    if initial_tour[0] != 0 or initial_tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 6 cities are visited
    unique_cities = set(initial_tour)
    if len(unique_cities) != 6:
        return "FAIL"
    
    # Check the correctness of the travel cost
    calculated_cost = evaluate_tour(initial_tour, city_coordinates)
    if abs(calculated_cost - initial_cost) > 0.001: # Using a tolerance for floating point arithmetic.
        return "FAIL"
    
    # Check if total number of cities including the depot is 10
    if total_cities != 10:
        return "FAIL"
    
    # No need to check if tour includes only valid indices, as all indices are assumed to be from 0 to total_cities-1
    
    return "CORRECT"

# Now we call the test function and print the result
print(test_solution())