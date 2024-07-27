import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(cities, tour, total_cost, max_distance):
    # Constant setup
    depot_city = 0
    
    # Check if the tour starts and ends at the depot, and all cities are visited once
    if tour[0] != depot_city or tour[-1] != depot_city or len(set(tour)) != len(cities):
        return "FAIL"
    
    # Check the number of cities visited (including depot twice)
    if len(tour) != len(cities) + 1:
        return "FAIL"
    
    # Compute total travel cost and maximum distance from the tour
    computed_total_cost = 0
    computed_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        computed_total_cost += distance
        if distance > computed_max_distance:
            computed_max_metadata_distance = distance
    
    # Check if computed values match given values
    if (not math.isclose(computed_total_cost, total_cost, rel_tol=1e-4) or 
        not math.isclose(computed_max_distance, max_distance, rel_tol=1e-4)):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of each city, including the depot city
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Tour information from the solution
tour = [0, 6, 14, 8, 11, 12, 2, 13, 7, 1, 9, 3, 5, 10, 4, 0]
total_travel_cost = 458.91046789880045
maximum_distance = 50.21951811795888

# Verification result
result = verify_solution([cities[i] for i in range(len(cities))], tour, total_travel_cost, maximum_distance)
print(result)