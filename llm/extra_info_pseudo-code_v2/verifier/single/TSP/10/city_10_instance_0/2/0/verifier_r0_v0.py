import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour_and_cost(tour, cost, cities):
    if len(tour) != len(set(tour)) + 1 or len(cities) != len(set(tour)) - 1:
        return False
    
    # Start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Calculating the total cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    
    # Comparing float with a tolerance due to floating point arithmetic issues
    if not math.isclose(calculated_cost, cost, abs_tol=1e-2):
        return False
    
    return True

# Cities' coordinates
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

# Provided solution
tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
total_travel_cost = 295.99

# Verification
if verify_tour_and_cost(tour, total_travel_cost, cities):
    print("CORRECT")
else:
    print("FAIL")