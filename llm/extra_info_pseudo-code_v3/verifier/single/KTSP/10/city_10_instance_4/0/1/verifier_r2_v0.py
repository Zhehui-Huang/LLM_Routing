import math

# Provided solution
solution_tour = [0, 4, 7, 5, 1, 9, 8, 3, 0]
provided_total_cost = 276.74

# City coordinates
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

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_solution(tour, total_cost):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if exactly 8 cities are visited, including the depot
    if len(set(tour)) != 9:
        return False

    # Compute the total travel cost and compare to provided
    calculated_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.1):
        return False

    return True

# Validate the solution
if check_solution(solution_tour, provided_total_cost):
    print("CORRECT")
else:
    print("FAIL")