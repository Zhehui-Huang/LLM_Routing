import math

def euclidean_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)

def verify_solution(tour, total_cost):
    # Given city coordinates
    city_coords = {
        0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28), 
        5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
    }

    # Check number of cities is 10
    if len(city_coords) != 10:
        return "FAIL"
    
    # Check robot starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check robot visits exactly 7 distinct cities including the depot at the start and end
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Check if the solution consists of exactly 7 cities
    if len(tour) != 7 + 1:  # Including the return to the depot
        return "FAIL"
    
    # Calculate total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = city_coords[tour[i]]
        city2 = city_coords[tour[i + 1]]
        calculated_cost += euclidean_distance(city1, city2)
    
    # Check against provided total cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 8, 3, 7, 1, 2, 4, 0]
total_travel_cost = 159.97188184793015

# Output the verification result
print(verify_solution(tour, total_travel_link_cost))