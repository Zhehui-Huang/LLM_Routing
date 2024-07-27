import math

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_travel_cost):
    cities_coordinates = {
        0: (14, 77),
        1: (34, 20),
        2: (19, 38),
        3: (14, 91),
        4: (68, 98),
        5: (45, 84),
        6: (4, 56),
        7: (54, 82),
        8: (37, 28),
        9: (27, 45),
        10: (90, 85),
        11: (98, 76),
        12: (6, 19),
        13: (26, 29),
        14: (21, 79),
        15: (49, 23),
        16: (78, 76),
        17: (68, 45),
        18: (50, 28),
        19: (69, 9)
    }
    
    # [The robot must visit exactly 7 cities, including the starting depot city.]
    if len(tour) != 8 or len(set(tour)) != 8:
        return "FAIL"
    
    # [The starting and ending point of the tour must be the depot city 0.]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate the travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += euclidean_distance(cities_coordinates[city1], cities_coordinates[city2])
    
    # [The output should include the exact path starting and ending at city 0.]
    # [The total travel distance is calculated using the Euclidean distance between the cities.]
    # [The output should also include the total travel cost of the selected tour.]
    if abs(calculated_cost - float(total_travel_cost)) > 0.01:  # Allowing for slight floating point arithmetic issues
        return "FAIL"
    
    return "CORRECT"

# Solution given
tour = [0, 6, 2, 13, 8, 9, 14, 0]
total_travel_cost = 130.67

# Invoke the verification function
result = verify_solution(tour, total_travel_cost)
print(result)