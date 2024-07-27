import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_cost, cities):
    # Requirement 1: Starts and ends at depot city (index 0)
    requirement_1 = tour is not None and len(tour) > 1 and tour[0] == 0 and tour[-1] == 0

    # Requirement 2: Visits exactly 6 cities including the depot
    requirement_2 = len(tour) == 7  # Includes depot city twice (start and end)

    # Requirement 3: Correct calculation of the total travel cost
    if tour is not None:
        calculated_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
        requirement_3 = abs(calculated_fcost - total_cost) < 1e-2  # Allowing a tiny margin for floating point errors
    else:
        requirement_3 = False

    # Requirement 4 and 5 are conceptual and assurance based on the output

    # Collectively assessing the output correctness
    return "CORRECT" if requirement_1 and requirement_2 and requirement_3 else "FAIL"

# City coordinates as given in the task
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Solution provided
tour = None  # This should be a list of indices if provided correctly
total_cost = 118.90

# Run the test function
result = test_solution(tour, total_cost, cities)
print(result)