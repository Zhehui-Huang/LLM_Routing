import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tour, total_cost, max_distance):
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once
    if len(set(tour)) != len(cities) or sorted(set(tour)) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Calculate actual distances and costs
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance
            
    # Check total travel cost and maximum distance between any two consecutive cities
    if not (math.isclose(actual_total_cost, total_cost, rel_tol=1e-2) and 
            math.isclose(actual_max_distance, max_distance, rel_tol=1e-2)):
        return "FAIL"
    
    return "CORRECT"

# Provided sample solution
cities = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]
tour_solution = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost_solution = 291.41
maximum_distance_solution = 56.61

# Check the solution
result = verify_solution(cities, tour_solution, total_travel_qual_cost_solicost_solution, mationtance_solution)
print(result)  # Should print "CORRECT" if all checks pass