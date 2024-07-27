import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour_requirements(tour, cities):
    # Extracting details from the solution provided
    tour_list = tour['Tour']
    total_travel_cost = tour['Total travel cost']
    max_distance_consecutive = tour['Maximum distance between consecutive cities']
    
    # [Requirement 1] Check if the tour starts and ends at the depot city 0
    if tour_list[0] != 0 or tour_list[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if each city is visited exactly once
    visited = set(tour_list[1:-1])  # Exclude the repeating depot city
    if len(visited) != len(cities) - 1 or any(city not in visited for city in range(1, len(cities))):
        return "FAIL"
    
    # [Requirement 5] Check if tour output is formatted correctly
    if not (tour_list[0] == 0 and tour_list[-1] == 0):
        return "FAIL"
    
    # Evaluate total distance and max distance between consecutive cities for verification against provided outputs
    calculated_max_distance = 0
    calculated_total_distance = 0
    
    for i in range(len(tour_list) - 1):
        d = euclidean_distance(cities[tour_list[i]], cities[tour_list[i+1]])
        calculated_total_distance += d
        if d > calculated_max_distance:
            calculated_max_distance = d

    # [Requirement 6] Check if total travel cost is correct
    if not math.isclose(calculated_total_with_precision, total_travel_cost, abs_tol=1e-5):
        return "FAIL"

    # [Requirement 7] Check if maximum distance between consecutive cities is as reported
    if not math.isclose(calculated_max_distance, max_distance_consecutive, abs_tol=1e-5):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Mock data simulating the output of your TSP or VRP solution
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 44), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Example output from your algorithm (this should be replaced with your actual solution output)
solution_output = {
    'Tour': [0, 1, 7, 12, 19, 16, 14, 13, 18, 15, 5, 17, 4, 3, 10, 8, 6, 11, 9, 2, 0],
    'Total travel cost': 450.324,
    'Maximum distance between consecutive, cities': 97.416
}

result = check_tour_requirements(solution_output, cities)
print(result)