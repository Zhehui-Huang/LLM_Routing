import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    cities = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
        (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
        (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
        (50, 28), (69, 9)
    ]
    
    # Check requirement: The robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check requirement: The robot must visit all cities exactly once, except the depot city
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"
    
    # Calculate the total travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check requirement: Travel cost calculation
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Define the proposed tour and total travel cost
proposed_tour = [0, 6, 12, 13, 2, 9, 8, 1, 15, 18, 19, 17, 16, 11, 10, 4, 7, 5, 14, 3, 0]
proposed_total_cost = 389.31

# Print verification result
print(verify_solution(proposed_tour, proposed_total_cost))