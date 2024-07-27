import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tour, total_cost):
    # Verify that the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify that the robot visits exactly 6 cities including the depot city
    if len(tour) - 1 != 6:  # Includes depot city at start and end = 7 positions total
        return "FAIL"
    
    # Verify that the tour only includes valid city indices
    if not all(city in cities for city in tour):
        return "FAIL"

    # Calculate the travel cost based on the tour provided
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Compare the calculated cost to the provided total cost with reasonable float precision
    if not math.isclose(total_cost, calculated_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Environment information - coordinates for 10 cities
cities = [
    (90, 3),  # City 0 - Depot
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Provided tour and total cost
tour = [0, 9, 1, 5, 8, 0]
total_travel_cost = 174.69223764340376

# Calling the verification function
result = verify submitted_solution(cities, tour, total_travel_cost)
print(result)