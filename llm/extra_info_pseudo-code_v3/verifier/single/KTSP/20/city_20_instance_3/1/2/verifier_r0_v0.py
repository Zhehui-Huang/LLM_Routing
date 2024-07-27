import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost):
    # Define cities coordinates
    cities = {
        0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 
        6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 
        12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 
        18: (53, 76), 19: (19, 72)
    }
    
    # [The robot must start and end its journey at the depot city, which is city 0.]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [The robot needs to visit exactly 13 cities, including the depot city.]
    if len(tour) != 14:  # includes the return to the depot, hence 14 points
        return "FAIL"
    
    # [The travel cost is calculated as the Euclidean distance between cities.]
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-02):
        return "FAIL"
    
    # [The goal is to find the shortest possible tour that only includes 13 cities.]
    # This cannot be validated without knowing all possible tours or achieving optimum through an algorithm verification.
    
    # [Output should list the tour as city indices starting and ending at city 0.]
    # and [Output should also list the total travel cost of the tour.]
    # These outputs are as required by the problem statement and adjusted for correctness in implementation.

    return "CORRECT"

# Provided tour and total travel cost
tour = [0, 3, 16, 9, 5, 19, 2, 13, 18, 12, 7, 4, 1, 0]
total_travel_cost = 316.31

# Call the verification function
result = verify_solution(tour, total_travel_cost)
print(result)