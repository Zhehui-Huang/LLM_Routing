import math

# Given data
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Solution to test
tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
total_cost_given = 45.00
max_distance_given = 45.19

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Check if the tour is correct
def test_tour():
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once except the depot city
    visited = set(tour)
    if len(visited) != 10 or any(city not in visited for city in cities.keys()):
        return "FAIL"
    
    # Calculate total cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        dist = euclidean_distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Check total cost and max distance against given values
    if not math.isclose(total_cost, total_cost_given, rel_tol=1e-2) or not math.isclose(max_distance, max_distance_given, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Run the test
test_result = test_tour()
print(test_result)