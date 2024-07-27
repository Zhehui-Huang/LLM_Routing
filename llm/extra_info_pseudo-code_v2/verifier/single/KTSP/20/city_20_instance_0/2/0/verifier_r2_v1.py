import math

def calculate_distance(city1, city2):
    # Calculate Euclidean distance between two points
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, total_cost):
    # Coordinates of the cities
    cities_coordinates = {
        0: (8, 11),
        1: (40, 6),
        2: (95, 33),
        3: (80, 60),
        4: (25, 18),
        5: (67, 23),
        6: (97, 32),
        7: (25, 71),
        8: (61, 16),
        9: (27, 91),
        10: (91, 46),
        11: (40, 87),
        12: (20, 97),
        13: (61, 25),
        14: (5, 59),
        15: (62, 88),
        16: (13, 43),
        17: (61, 28),
        18: (60, 63),
        19: (93, 15)
    }

    # Check if the tour starts and ends at the depot city (city 0), and exact number of cities visited
    if tour[0] != 0 or tour[-1] != 0 or len(set(tour)) != 4:
        return "FAIL"
    
    # Calculate the total travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])

    # Comparing the given total travel cost with the calculated cost
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Read the provided tour and total cost
solution_tour = [0, 1, 1, 1, 0]
solution_total_cost = 64.78

# Validate the solution
print(check_solution(solution_tour, solution_total_cost))