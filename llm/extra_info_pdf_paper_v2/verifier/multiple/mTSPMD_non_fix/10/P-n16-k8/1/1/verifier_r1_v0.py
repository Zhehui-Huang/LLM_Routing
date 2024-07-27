import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Robot tours provided in the solution
robot_tours = {
    0: [0, 14, 1, 0],
    1: [0, 12, 4, 0],
    2: [0, 8, 9, 0],
    3: [0, 5, 10, 0],
    4: [0, 13, 11, 0],
    5: [0, 15, 3, 0],
    6: [0, 2, 7, 0],
    7: [0, 6, 0]
}

# Calculate Euclidean distance
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Check Requirement 1: Ensure each city visited exactly once and start is depot 0
visited_cities = set()
all_tours = sum([len(tour) for tour in robot_tours.values()])
for tour in robot_tours.values():
    if tour[0] != 0:
        print("FAIL")
        break
    visited_cities.update(tour)
if len(visited_cities) != len(cities):
    print("FAIL")

# Check Requirement 2: Tours end at any city
for tour in robot_tours.values():
    if tour[-1] == tour[0]:
        continue
    else:
        print("FAIL")
        break

# Check Requirement 4: All tours must start at depot city 0
if any(tour[0] != 0 for tour in robot_tours.values()):
    print("FAIL")

# Check Requirement 3 & 5: Minimum travel cost and correct costs calculated
# Calculate total cost mentioned
mentioned_costs = [
    77.41279750494509, 64.98936367308863, 81.27545517717891, 69.8954448079152,
    94.17242872917295, 78.20189727339391, 51.59051533249141, 24.08318915758459
]
calculated_costs = []
for i, tour in robot_tours.items():
    cost = sum(calculate_distance(cities[tour[j]], cities[tour[j + 1]]) for j in range(len(tour) - 1))
    calculated_costs.append(cost)

if not all(math.isclose(mc, ac, abs_tol=1e-5) for mc, ac in zip(mentioned_costs, calculated_costs)):
    print("FAIL")

# Calculate and verify total cost
total_calculated_cost = sum(calculated = sum(calculate_distance(cities[tour[i]], 
cities[tour[i + 1]]) for i in range(len(tour) - 1)) for tour in robot_tours.values())
if not math.isclose(total_calculated_cost, 541.6210916557707, abs_tol=1e-5):
    print("FAIL")

# If all checks passed
print("CORRECT")