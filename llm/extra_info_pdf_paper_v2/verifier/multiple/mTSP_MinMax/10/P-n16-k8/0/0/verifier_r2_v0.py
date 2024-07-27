import math

# Define the function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates (indexed from 0 to 15)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64),
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Solution proposed
solution_tours = [
    [0, 4, 7, 0],
    [0, 13, 5, 0],
    [0, 8, 3, 0],
    [0, 14, 11, 0],
    [0, 1, 10, 0],
    [0, 12, 15, 0],
    [0, 6, 2, 0],
    [0, 9, 0]
]

solution_costs = [73.74391590092547, 68.36272673975597, 72.81785234728197,
                  110.4313428651093, 41.77216384800009, 66.12407122823275,
                  43.69553643315558, 64.1248781675256]

# Verifying Requirement 1 and 5
total_cities_visited = set()
actual_costs_calculated = []
for tour in solution_tours:
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL")
        break
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    actual_costs_calculated.append(cost)
    total_cities_visited.update(tour)

# Verifying Requirement 2
if len(total_cities_visited) == 16 and all(city in total_cities_visited for city in range(16)):
    pass # Requirement satisfied
else:
    print("FAIL")

# Verifying Requirement 3
max_cost_reported = 110.4313428651093
if math.isclose(max(solution_costs), max_cost_reported, rel_tol=1e-9):
    pass # Requirement satisfied
else:
    print("FAIL")

# Verifying Requirement 4
if len(solution_tours) == 8:
    pass # Correct number of robots
else:
    print("FAIL")

# Output checking
if all(math.isclose(expected, actual, rel_tol=1e-9) for expected, actual in zip(solution_costs, actual_costs_calculated)):
    print("CORRECT")
else:
      print("FAIL")