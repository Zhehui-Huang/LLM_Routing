import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += calculate_euclidean_distance(*coordinates[city1], *coordinates[city2])
    return total_cost
    
def verify_solution(tour, expected_cost, coordinates):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour visits exactly 6 cities including the depot
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Check if the total number of vertices visited is 7 (6 cities + 1 return to depot)
    if len(tour) != 7:
        return "FAIL"
    
    # Check the travel cost calculation
    calculated_cost = calculate_total_travel_cost(tour, coordinates)
    if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

coordinates = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
   10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}
solution_tour = [0, 6, 1, 7, 3, 9, 0]
expected_cost = 118.8954868377263

# Call the verification function and print the result
result = verify_solution(solution_tour, expected_cost, coordinates)
print(result)