import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    """ Compute Euclidean distance between two points (x1, y1) and (x2, y2). """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_solution(tour, total_cost):
    # Define the cities coordinates
    cities = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }

    # [Requirement 1]: The robot must start and end the tour at the depot city, which is city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]: The robot has to visit exactly 8 cities, including the depot city.
    if len(tour) != 9 or len(set(tour)) != 9:  # including repetitions
        return "FAIL"

    # [Requirement 3 & 4]: The objective is to find the shortest tour based on the Euclidean distance between cities
    # and compute the total travel cost of the tour.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Compare the computed cost to the provided total travel cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Test the given solution
tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
total_cost = 235.38
print(check_solution(tour, total_cost))