def compute_euclidean_distance(city1, city2):
    from math import sqrt
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # City coordinates
    cities = [
        (53, 68),  # Depot city 0
        (75, 11),  # City 1
        (91, 95),  # City 2
        (22, 80),  # City 3
        (18, 63),  # City 4
        (54, 91),  # City 5
        (70, 14),  # City 6
        (97, 44),  # City 7
        (17, 69),  # City 8
        (95, 89)   # City 9
    ]

    # Requirement 1: Tour must start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: The robot must visit exactly 5 cities, including the depot city
    if len(set(tour)) != 5:
        return "FAIL"

    # Calculate the euclidean travel cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += compute_euclidean_distance(cities[tour[i-1]], cities[tour[i]])

    # Requirement 3: Check if calculated total cost matches the provided total cost
    # Allowing a small margin for floating point comparison
    if abs(calculated_cost - total_cost) > 0.001:
        return "FAIL"

    # If all conditions are met
    return "CORRECT"

# Solution details
tour_provided = [0, 4, 8, 3, 5, 0]
total_cost_provided = 110.38072506104011

# Check the solution
result = verify_solution(tour_provided, total_cost_provided)
print(result)