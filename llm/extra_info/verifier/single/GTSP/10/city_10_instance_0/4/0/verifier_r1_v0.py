import math

# Data
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

city_groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Provided tour and cost
provided_tour = [0, 5, 6, 7, 0]
provided_cost = 72.82824391360948

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour(tour, expected_cost):
    # Check if tour starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check the total cost
    total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-6):
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited = set(tour[1:-1])  # excluding the starting and ending depot city
    for group in city_groups.values():
        if sum(c in visited for c in group) != 1:
            return "FAIL"
    
    return "CORRECT"

# Testing the provided solution against the stated requirements
result = verify_tour(provided_tour, provided_cost)
print(result)