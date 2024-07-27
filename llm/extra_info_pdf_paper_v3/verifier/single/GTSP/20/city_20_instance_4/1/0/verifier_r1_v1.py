import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # Coordinates for each city
    cities = {
        0: (26, 60), 
        1: (73, 84),
        2: (89, 36),
        3: (15, 0),
        4: (11, 10),
        5: (69, 22),
        6: (28, 11),
        7: (70, 2),
        8: (47, 50),
        9: (60, 29),
        10: (29, 26),
        11: (85, 68),
        12: (60, 1),
        13: (71, 73),
        14: (82, 47),
        15: (19, 25),
        16: (75, 9),
        17: (52, 54),
        18: (64, 72),
        19: (14, 89)
    }

    # City groups
    city_groups = [
        [5, 6, 16],
        [8, 18, 19],
        [11, 12, 13],
        [1, 3, 9],
        [2, 4, 14],
        [10, 17],
        [7, 15]
    ]

    # Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate total travel cost
    calculated_total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

    # Check if calculated total cost is approximately equal to the given total cost
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
        
    visited_groups = set()
    for city in tour[1:-1]:  # excluding the depot city
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(i)
                
    # Check if the robot visits exactly one city from each group
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    return "CORRECT"

# Provided tour and calculated total travel cost
provided_tour = [0, 15, 4, 6, 12, 9, 17, 8, 0]
provided_total_cost = 187.15997262302855

# Validation of the solution
print(verify_solution(provided_tour, provided_total_cost))