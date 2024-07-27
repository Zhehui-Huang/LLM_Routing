import math

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Provided solution
solution_tour = [0, 10, 1, 8, 0, 10, 1, 8, 0, 10, 1, 8, 0, 10, 1, 0]
solution_cost = 373.26667878524154
solution_max_distance = 42.01190307520001

# Cities coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Validate tour
if solution_tour[0] != 0 or solution_tour[-1] != 0:
    print("FAIL")
else:
    # Check if all cities are visited exactly once
    city_visit_count = {i: 0 for i in range(len(cities))}
    for city in solution_tour:
        city_visit_count[city] += 1

    if any(count > 1 for i, count in city_visit_count.items() if i != 0):
        print("FAIL")
    else:
        # Check total travel cost and max distance
        calculated_cost = 0
        calculated_max_distance = 0
        for i in range(len(solution_tour) - 1):
            distance = compute_distance(cities[solution_tour[i]], cities[solution_tour[i+1]])
            calculated_cost += distance
            if distance > calculated_max_distance:
                calculated_max_distance = distance

        if (abs(calculated_cost - solution_cost) > 1e-5 or
            abs(calculated_max_distance - solution_max_distance) > 1e-5):
            print("FAIL")
        else:
            print("CORRECT")