import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_cost, city_coordinates):
    # Checks if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Checks if the tour includes exactly 6 cities including the depot
    if len(tour) != 6:
        return "FAIL"
    
    # Validate if calculated total cost matches the expected total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    if not math.isclose(total_cost, calculated_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# City coordinates provided in the problem description
city_coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Solution provided for verification
tour = [0, 2, 7, 6, 3, 0]
total_cost = 308.8045184787742

# Verifying the solution
result = verify_solution(tour, total_cost, city_coordinates)
print(result)