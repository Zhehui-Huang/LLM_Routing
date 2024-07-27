import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, total_cost, max_dist):
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76),
    }
    
    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour) != sorted(list(cities.keys())):
        return "FAIL"
    
    # Compute distances
    distances = [calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1)]
    
    # [Requirement 3]
    computed_total_cost = sum(distances)
    if not math.isclose(computed_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # [Requirement 5]
    computed_max_dist = max(distances)
    if not math.isclose(computed_max_dist, max_dist, rel_tol=1e-5):
        return "FAIL"
    
    # [Requirement 4]
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Check for any other requirement may go here...
    
    return "CORRECT"

# Provided solution
tour = [0, 1, 2, 3, 9, 5, 6, 7, 4, 8, 0]
total_travel_cost = 421.9753959772767
maximum_distance = 69.06518659932803

# Verify the solution
result = verify_solution(tour, total_travel_cost, maximum_distance)
print(result)