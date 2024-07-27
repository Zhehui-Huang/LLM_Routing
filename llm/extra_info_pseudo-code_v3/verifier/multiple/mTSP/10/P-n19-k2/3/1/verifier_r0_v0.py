import math

# City coordinates and robot tour data
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

robot_tours = {
    0: [0, 1, 4, 3, 2, 5, 6, 7, 8, 9, 0],
    1: [0, 10, 11, 12, 14, 13, 15, 16, 17, 18, 0]
}

reported_costs = {
    0: 167.65466815291444,
    1: 205.81271460072625
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Check unique city visitation excluding depot (city 0)
all_cities_visited = set()
for tour in robot_tours.values():
    all_cities_visited.update(tour[1:-1])  # Exclude the depot city from the start and end

# Test 1: Check all cities are visited exactly once
cities_correctly_visited = (all_cities_visited == set(city_coordinates.keys()) - {0})

# Test 2: Check tours start and end at the depot city
tours_correct_structure = all(tour[0] == 0 and tour[-1] == 0 for tour in robot_tours.values())

# Test 3: Verify calculated travel costs
costs_correct = True
for robot_id, tour in robot_tours.items():
    computed_cost = sum(euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    costs_correct &= (abs(computed_cost - reported_costs[robot_id]) < 1e-6)  # Use a tolerance for floating-point comparison

# Result output based on tests
if cities_correctly_visited and tours_correct_structure and costs_correct:
    result = "CORRECT"
else:
    result = "FAIL"
    
print(result)