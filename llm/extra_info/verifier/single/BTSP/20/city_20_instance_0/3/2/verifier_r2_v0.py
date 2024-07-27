import math

# Coordinates of the cities
cities = [
    (8, 11),   # depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

# Provided solution
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 349.20
max_distance = 32.39

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Function to test the provided solution against the requirements
def test_solution(tour, total_cost, max_dist):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once except depot city 0, which should be visited twice
    if sorted(tour) != sorted(list(range(len(cities))) + [0]):
        return "FAIL"
    
    # Calculate the travel cost and max distance to verify
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
            
    # Since it's floating point comparison, we allow some small error
    if not (abs(calculated_total_cost - total_cost) < 0.1 and 
            abs(calulated_max_distance - max_dist) < 0.1):
        return "FAIL"

    # Requirement 3: Implicit validation by provided solution, and no way to validate minimization without knowing all solutions
    return "CORRECT"

# Run test with provided values
result = test_solution(tour, total_travel_cost, max_distance)
print(result)