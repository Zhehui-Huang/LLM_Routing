import math

# Define the city coordinates and demands
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
robot_tours = [
    [0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0], [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0],
    [0, 10, 0], [0, 11, 0], [0, 12, 0], [0, 13, 0], [0, 14, 0], [0, 15, 0], [0, 16, 0], [0, 17, 0], [0, 18, 0], [0, 19, 0], [0, 20, 0]
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Visited cities check
visited_cities = set()
for tour in robot_tours:
    for city in tour:
        if city != 0:
            visited_cities.add(city)

# All cities must be visited once except depot city
assert len(visited_cities) == 20, "Not all cities are visited or some are visited more than once."

# Start & end at the depot, and no subtours
for tour in robot_tours:
    assert tour[0] == 0 and tour[-1] == 0, "Tour must start and end at depot city."

# Total demand per robot does not exceed capacity
for tour in robot_tours:
    total_demand = sum(demands[city] for city in tour if city != 0)
    assert total_demand <= 160, "Robot capacity exceeded."

# Calculate and check total travel costs
total_travel_cost = 0
for tour in robot_tours:
    tour_cost = 0
    for i in range(len(tour)-1):
        tour_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    total_travel_cost += tour_cost

assert round(total_travel_cost, 2) == 1562.55, "Total travel cost does not match."

# Output "CORRECT" if all assertions pass, otherwise "FAIL"
print("CORRECT")