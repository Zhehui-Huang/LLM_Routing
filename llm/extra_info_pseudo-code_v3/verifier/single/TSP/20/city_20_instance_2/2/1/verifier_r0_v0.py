import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, total_travel_cost):
    # Define city coordinates
    cities = [
        (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
        (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
        (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
    ]

    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once except depot
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"

    # Calculate the total cost from the tour indices
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check if the calculated cost matches the given cost
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    # Since the solution satisfies all requirements
    return "CORRECT"

# Example solution data
tour_example = [0, 14, 16, 11, 7, 10, 3, 4, 1, 19, 17, 5, 6, 8, 2, 9, 15, 13, 18, 12, 0]
total_travel_cost_example = 692.5810597504949

# Check the solution using the provided example
result = check_solution(tour_example, total_travel_cost_example)
print(result)