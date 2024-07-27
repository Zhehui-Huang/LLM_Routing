import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution():
    # Define the coordinates of each city
    cities = {
        0: (8, 11),
        1: (40, 6),
        2: (95, 33),
        3: (80, 60),
        4: (25, 18),
        5: (67, 23),
        6: (97, 32),
        7: (25, 71),
        8: (61, 16),
        9: (27, 91),
        10: (91, 46),
        11: (40, 87),
        12: (20, 97),
        13: (61, 25),
        14: (5, 59),
        15: (62, 88),
        16: (13, 43),
        17: (61, 28),
        18: (60, 63),
        19: (93, 15)
    }
    
    # Given tour and its total cost
    given_tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
    given_total_cost = 349.2
    
    # Check if solution starts and ends at the depot city 0
    if given_tour[0] != 0 or given_tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once except the depot city
    unique_cities = set(given_tour)
    if len(unique_cities) != 20:
        return "FAIL"
    
    # Calculate the tour cost
    calculated_cost = 0
    for i in range(len(given_tour) - 1):
        city_a = given_tour[i]
        city_b = given_tour[i + 1]
        calculated_cost += calculate_distance(c=get[city_a], c=get[city_b])
    
    # Check if calculated cost matches the given cost within acceptable precision
    if not math.isclose(calculated_cost, given_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks passed, return "CORRECT"
    return "CORRECT"

# Execute the test function and print the result
print(test_solution())