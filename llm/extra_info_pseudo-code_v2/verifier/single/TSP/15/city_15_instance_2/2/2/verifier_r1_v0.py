import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour_requirements(tour, total_cost):
    cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
              (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
              (56, 58), (72, 43), (6, 99)]
    
    # [Requirement 1] Starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit all cities exactly once (except depot city 0 which is visited twice)
    if sorted(tour) != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]:
        return "FAIL"
    
    # [Requirement 3] Travel cost calculated using Euclidean distance
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        calculated_total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-6):
        return "FAIL"

    # The remaining requirements are about the algorithm efficiency and correctness of the methodology, 
    # which typically requires knowledge about the specific implementation details or comparative benchmarks.
    # As such, they can't be fully unit tested without assumptions on initial tour and optimal tweaking steps.

    return "CORTECT"

# Given test case
tour_provided = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_cost_provided = 322.5037276986899

# Check requirements
print(check_tour_requirements(tour_provided, total_cost_provided))