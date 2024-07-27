import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def test_solution(tour, total_travel_cost):
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
        9: (95, 89)
    }
    
    # Requirement 1: The robot must start and end its tour at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot must visit a total of 5 cities, including the depot city
    if len(tour) != 6:
        return "FAIL"
    
    # Requirement 3: Calculate travel cost using the Euclidean distance between cities
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if abs(calculated_cost - total_travel_cost) > 1e-5:  # Allowing a small precision error
        return "FAIL"
    
    # Requirement 4: The robot's tour exactly contains 5 cities
    if len(set(tour)) != 6:  # Including repeated depot city 0
        return "FAIL"
    
    # Requirement 5: Robot can travel between any two cities is inherent in the setup and thus passed by default.

    return "CORRECT"

# Testing the provided solution
tour = [0, 4, 8, 3, 5, 0]
total_travel_cost = 110.38072506104011
print(test_solution(tour, total_travel_cost))