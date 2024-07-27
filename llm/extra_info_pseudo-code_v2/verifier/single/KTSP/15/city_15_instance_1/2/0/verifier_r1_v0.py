import math

# Define the coordinates of the cities
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Tentative proposed solution
tour = [0, 7, 1, 8, 2, 11, 0]
proposed_total_cost = 205.09

# Perform tests
def test_tour():
    # Requirements checking
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(tour) != 7:
        return "FAIL"
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Calculate the total distance
    total_distance = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    # Check if the returned travel cost correctly corresponds to the calculated cost
    if not math.isclose(total_distance, proposed_total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Run the test for the proposed solution
test_result = test_tour()
print(test_result)