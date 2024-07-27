import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tour, total_cost):
    # Verify tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify robot visits exactly 6 cities including the depot city
    if len(tour) != 7:  # 6 cities + 1 repetition of depot
        return "FAIL"
    
    # Verify only existing city indices are toured
    if not all(city in range(len(cities)) for city in tour):
        return "FAIL"

    # Calculate the total travel cost from the tour and compare it to the given total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Comparing the calculated cost and provided cost with a tolerance due to float precision
    if not math.isclose(calculated[total_cost, calculated_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Environment information
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Provided tour and cost
tour = [0, 9, 1, 5, 8, 0]
total_travel_cost = 174.69223764340376

# Call the verification function
result = verify_solution(cities, tour, total_travel_cost)
print(result)