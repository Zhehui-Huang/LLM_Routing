import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_travel_cost):
    cities = { 
        0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84), 
        6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76), 
        12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68,45), 
        18: (50, 28), 19: (69, 9)
    }

    # Check requirement: The robot needs to visit exactly 7 cities including the depot city 0
    if len(tour) != 8 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check requirement: The tour must start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check requirement: The goal is to find the shortest possible tour
    # Here we cannot validate if it's the absolutely shortest tour but can check if calculated cost matches given cost
    if not math.isclose(computed_cost, total_travel_cost, abs_tol=0.1):
        return "FAIL"

    return "CORRECT"

# Given tour and cost
tour_solution = [0, 3, 14, 5, 9, 2, 6, 0]
total_cost_solution = 152.68

# Verify the solution
result = verify_tour(tour_solution, total_cost_solution)
print(result)