import math

def compute_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour_properties(cities, tour, expected_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 8 cities are visited including the starting city
    if len(set(tour)) != 8:
        return "FAIL"
    
    # Check if the total number of cities is 15
    if len(cities) != 15:
        return "FAIL"

    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += compute_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if calculated total cost matches the given expected total cost
    if math.isclose(total_cost, expected_cost, rel_tol=1e-2):
        return "CORRECT"
    else:
        return "FAIL"

# City coordinates
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

# Solution provided details
tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
total_cost = 132.12

# Verify solution
result = verify_tour_properties([cities[i] for i in range(15)], tour, total_cost)
print(result)