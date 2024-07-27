import math
from collections import Counter

# Define the city coordinates based on the environment information provided
coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35),
}

# Tours provided by the solution
tours = {
    0: [0, 1, 10, 2, 7, 9, 15, 13, 5, 18, 6, 0],
    1: [0, 8, 16, 17, 3, 12, 14, 11, 4, 0]
}

# Utility to calculate the Euclidean distance between two cities
def calculate_distance(c1, c2):
    return round(math.sqrt((coordinates[c1][0] - coordinates[c2][0]) ** 2 + (coordinates[c1][1] - coordinates[c2][1]) ** 2))

# Check if each city is visited exactly once by one salesman
all_cities_in_tours = [city for tour in tours.values() for city in tour if city != 0]
city_count = Counter(all_cities_in_tours)

# Check the number of visits for each city
each_city_visited_once = all(city_count[city] == 1 for city in range(1, 19))

# Check if each salesman leaves the depot exactly once and returns exactly once
depot_leaves_returns_correctly = all(tour.count(0) == 2 and tour[0] == 0 and tour[-1] == 0 for tour in tours.values())

def all_visited_nodes_connected_correctly():
    for tour in tours.values():
        for i in range(len(tour) - 1):
            if calculate_distance(tour[i], tour[i + 1]) == 0:
                return False
    return True

# Check if each tour satisfies the subtour elimination (assuming correct input there are no subtours)
def check_subtour_elimination():
    for tour in tours.values():
        visited = set()
        for city in tour:
            if city in visited and visited != set(range(1, 19)):
                return False
            visited.add(city)
    return True

# Verify all conditions
correct_solution = (each_city_street_once and depot_leaves_returns_correctly
                    and all_visited_nodes_connected_correctly() and check_subtour_elimination())

# Print the output based on the result
output = "CORRECT" if correct_solution else "FAIL"
print(output)