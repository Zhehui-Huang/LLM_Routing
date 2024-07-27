import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cities, total_cost, max_dist):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city visited exactly once
    visited_cities = tour[1:-1]  # Exclude the repeated depot city
    if sorted(visited_cities) != list(range(1, len(cities))):
        return "FAIL"
    
    # Requirement 3 & 5 Check total travel cost and maximum distance correctness
    computed_costs = []
    for i in range(len(tour) - 1):
        computed_costs.append(euclidean_distance(cities[tour[i]], cities[tour[i+1]]))
    
    computed_total_cost = round(sum(computed_costs), 2)
    computed_max_dist = round(max(computed_costs), 2)
    
    # Requirement 4 Checked implicitly by using the Euclidean distance for calculations
    if computed_total_cost != total_cost or computed_max_dist != max_dist:
        return "FAIL"
    
    return "CORRECT"

# Coordinates for each city indexed from 0-9
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
tour = [0, 7, 6, 5, 9, 1, 2, 4, 8, 3, 0]
total_travel_cost = 370.9
maximum_distance = 76.94

# Validate the solution
result = verify_solution(tour, cities, total_travel_aggregate_cost=total_travel_cost, maximum_distance_between_cities=maximum_distance)
print(result)  # Expected output: CORRECT or FAIL based on verification