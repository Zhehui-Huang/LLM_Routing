import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities, tour, reported_cost):
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour includes exactly 8 cities
    if len(set(tour)) != 8:
        return "FAIL"
    
    # Check the total distance
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(total_distance, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

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

# Tour given in the solution
tour = [0, 12, 13, 9, 10, 3, 4, 2, 0]
reported_cost = 176.5947316099428

# Validate the tour
result = verify_tour(cities, tour, reported_cost)
print(result)