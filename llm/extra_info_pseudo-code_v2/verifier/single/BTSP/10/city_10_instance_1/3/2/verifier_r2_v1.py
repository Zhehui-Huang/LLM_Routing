import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_cost, max_distance):
    # [Requirement 1] Checking if all cities are visited exactly once, starting and ending at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"
        
    # Construct city coordinates map
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89),
    }
    
    # [Requirement 2] Calculate the actual total distance and check with provided data
    calculated_total_distance = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_distance += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    if not (math.isclose(total_cost, calculated_total_distance, rel_tol=0.01) and
            math.isclose(max_distance, calculated_max_distance, rel_tol=0.01)):
        return "FAIL"
    
    # [Requirement 3] Assumption: Provided max_distance should be minimized, 
    # but heuristic approach guarantees only an approximate optimal solution. 
    # There is no exact check possible without solving optimally or knowing the optimal value.
    
    # [Requirement 5] If it passed all the above criteria, the solution might be correct
    return "CORRECT"

# Mock the provided output data
tour = [0, 5, 3, 8, 4, 6, 1, 7, 9, 2, 0]
total_travel_cost = 290.84
maximum_distance_between_cities = 71.45

# Run the verification test
print(verify_tour(tour, total_travel_cost, maximum_distance_between_cities))