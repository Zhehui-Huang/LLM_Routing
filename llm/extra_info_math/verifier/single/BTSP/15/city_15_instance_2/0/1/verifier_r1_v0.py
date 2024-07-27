import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, cities):
    # [Requirement 1] The robot must visit each city exactly once and return to the depot city at the end
    if sorted(tour) != list(range(len(cities))) or tour[0] != tour[-1]:
        return "FAIL"

    # [Requirement 3] The cost of travel between any two cities i and j is the Euclidean distance between them
    total_cost_calculated = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    
    # [Requirement 2] The objective is to minimize the longest distance between any two consecutive cities in the tour
    max_distance_calculated = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

    if abs(total_cost_calculated - 370.74411296483567) > 0.001:
        return "FAIL"
    if abs(max_distance_calculated - 39.05124837953327) > 0.001:
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Tour provided by the solution
tour = [0, 2, 6, 1, 14, 8, 11, 4, 13, 7, 9, 3, 10, 5, 12, 0]

# Call verification function
result = verify_solution(tour, cities)
print(result)