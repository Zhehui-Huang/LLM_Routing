import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(solution_tour, reported_total_cost):
    city_coordinates = {
        0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
        5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
        10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
    }
    
    # Check if start and end city is the depot (city 0).
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 8 cities are visited (including start and end at city 0).
    if len(set(solution_tour)) != 9:  # Including city 0 twice (start and end)
        return "FAIL"
    
    # Calculate the total travel cost from the tour.
    total_cost = 0
    for i in range(len(solution_tour) - 1):
        city_index1 = solution_tour[i]
        city_index2 = solution_tour[i + 1]
        total_cost += calculate_distance(city_coordinates[city_index1], city_coordinates[city_index2])
    
    # Check if calculated total cost is close to the reported cost.
    if not math.isclose(total_cost, reported_total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Solution provided
solution_tour = [0, 6, 13, 10, 4, 3, 12, 11, 0]
reported_total_tour_cost = 146.82

# Perform the verification
result = verify_tour(solution_tour, reported_total_tour_cost)
print(result)