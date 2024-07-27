import math

# Input data
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Solution from the provided data
tour = [0, 12, 10, 13, 3, 4, 11, 6, 0]
calculated_cost = 159.017828545213

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Verify the solution
def verify_solution(tour, calculated_cost):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the tour visits exactly 8 cities (including the depot twice)
    if len(set(tour)) != 8:
        return "FAIL"

    # Calculate the actual travel cost and compare with the calculated cost
    actual_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if abs(actual_cost - calculated_cost) > 1e-6:
        return "FAIL"

    # If all checks pass, return "CORRECT"
    return "CORRECT"

# Call the verification function and print the result
result = verify_solution(tour, calculated_cost)
print(result)