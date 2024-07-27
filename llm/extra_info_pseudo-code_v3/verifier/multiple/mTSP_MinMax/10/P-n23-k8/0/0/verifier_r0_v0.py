import math

# City coordinates including depot
cities = [
    (30, 40),  # Depot
    (37, 52),  # 1
    (49, 49),  # 2
    (52, 64),  # 3
    (31, 62),  # 4
    (52, 33),  # 5
    (42, 41),  # 6
    (52, 41),  # 7
    (57, 58),  # 8
    (62, 42),  # 9
    (42, 57),  # 10
    (27, 68),  # 11
    (43, 67),  # 12
    (58, 48),  # 13
    (58, 27),  # 14
    (37, 69),  # 15
    (38, 46),  # 16
    (61, 33),  # 17
    (62, 63),  # 18
    (63, 69),  # 19
    (45, 35),  # 20
    (32, 39),  # 21
    (56, 37)   # 22
]

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Provided tour data
robot_tours = [
    [0, 2, 8, 13, 9, 0],
    [0, 15, 12, 3, 0],
    [0, 21, 6, 0],
    [0, 14, 17, 0],
    [0, 16, 10, 1, 0],
    [0, 18, 19, 0],
    [0, 4, 11, 0],
    [0, 20, 5, 22, 7, 0]
]

# Verify requirement 3: visit every city exactly once, excluding depot
visited_cities = set()
for tour in robot_tours:
    for city in tour[1:-1]:  # excluding depot at start and end
        visited_cities.add(city)

# Calculate travel cost for each tour to check requirement 5 and 6
robot_costs = []
for tour in robot_tours:
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    robot_costs.append(round(total_cost, 2))  # round for comparison to provided costs

# Check for maximum travel cost to satisfy requirement 4
max_cost = max(robot_costs)

# Check if all cities are visited once and total city count excluding depot is appropriate
all_cities_visited = (len(visited_cities) == 22 and all(city in visited_cities for city in range(1, 23)))

# Check the correctness of all requirements
solution_correct = all([
    len(cities) == 23,  # requirement 1
    len(robot_tours) == 8,  # requirement 2
    all_cities_visited,  # requirement 3 continuation
    max_cost == 89.42,  # requirement 4 and 7: given in output, ensuring the values match
    robot_costs == [82.39, 78.20, 24.48, 69.36, 42.67, 89.42, 57.39, 56.43]
])

print("CORRECT" if solution_correct else "FAIL")